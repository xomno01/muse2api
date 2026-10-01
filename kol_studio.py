"""MuseKOL Studio — Backend Engine for Virtual AI Influencer Creation & Production.

Integrates Meta Muse image/video/chat models with Edge-TTS voice generation,
FFmpeg media muxing, Face Anchor consistency, and Lookbook presets.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import shutil
import subprocess
import time
import uuid
from typing import Any, Dict, List, Optional

import edge_tts
from fastapi import APIRouter, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

log = logging.getLogger("muse2api.kol")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KOL_DIR = os.path.join(BASE_DIR, "data", "kol")
PROFILES_FILE = os.path.join(KOL_DIR, "profiles.json")
PRESETS_FILE = os.path.join(BASE_DIR, "kol_presets.json")
ANCHORS_DIR = os.path.join(KOL_DIR, "anchors")
GALLERY_DIR = os.path.join(KOL_DIR, "gallery")
AUDIO_DIR = os.path.join(KOL_DIR, "audio")
VIDEOS_DIR = os.path.join(KOL_DIR, "videos")

for d in (KOL_DIR, ANCHORS_DIR, GALLERY_DIR, AUDIO_DIR, VIDEOS_DIR):
    os.makedirs(d, exist_ok=True)

FFMPEG_BIN = "ffmpeg"
for candidate in [
    r"C:\ProgramData\chocolatey\bin\ffmpeg.exe",
    r"C:\ffmpeg\bin\ffmpeg.exe",
    "ffmpeg",
]:
    if shutil.which(candidate) or os.path.exists(candidate):
        FFMPEG_BIN = candidate
        break

router = APIRouter(prefix="/kol/api", tags=["KOL Studio"])


def _load_presets() -> dict:
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log.warning("Failed to load presets: %s", e)
    return {"characters": [], "lookbook_scenes": [], "motion_presets": [], "voices": [], "caption_styles": []}


def _load_profiles() -> list[dict]:
    if os.path.exists(PROFILES_FILE):
        try:
            with open(PROFILES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log.warning("Failed to load profiles: %s", e)
    presets = _load_presets()
    starter = presets.get("characters", [])
    now = int(time.time())
    for s in starter:
        s.setdefault("created_at", now)
        s.setdefault("face_anchor_url", None)
        s.setdefault("gallery_count", 0)
    with open(PROFILES_FILE, "w", encoding="utf-8") as f:
        json.dump(starter, f, ensure_ascii=False, indent=2)
    return starter


def _save_profiles(profiles: list[dict]):
    with open(PROFILES_FILE, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=2)


# ===================== Schemas =====================
class ProfileCreateReq(BaseModel):
    id: Optional[str] = None
    name: str
    tagline: Optional[str] = ""
    age: Optional[int] = 21
    archetype: Optional[str] = "Nàng thơ"
    nationality: Optional[str] = "Việt Nam"
    voice: Optional[str] = "vi-VN-HoaiMyNeural"
    dna_prompt: str
    negative_prompt: Optional[str] = ""
    bio: Optional[str] = ""
    personality_tone: Optional[str] = ""


class GenerateImageReq(BaseModel):
    profile_id: str
    scene_id: Optional[str] = None
    custom_prompt: Optional[str] = ""
    aspect_ratio: Optional[str] = "1:1"
    use_face_anchor: Optional[bool] = True


class GenerateVideoReq(BaseModel):
    profile_id: str
    image_url: str
    motion_id: Optional[str] = None
    custom_motion: Optional[str] = ""
    duration: Optional[int] = 5
    aspect_ratio: Optional[str] = "9:16"


class VoiceReq(BaseModel):
    text: str
    voice_id: Optional[str] = "vi-VN-HoaiMyNeural"
    rate: Optional[str] = "+0%"
    pitch: Optional[str] = "+0Hz"


class MuxReq(BaseModel):
    video_url: str
    audio_url: str


class CaptionReq(BaseModel):
    profile_id: str
    style_id: str
    topic: Optional[str] = ""
    scene_name: Optional[str] = ""


# ===================== Endpoints =====================
@router.get("/presets")
def get_presets():
    return _load_presets()


@router.get("/profiles")
def get_profiles():
    profiles = _load_profiles()
    for p in profiles:
        pid = p["id"]
        p_gallery = os.path.join(GALLERY_DIR, pid)
        if os.path.exists(p_gallery):
            p["gallery_count"] = len([f for f in os.listdir(p_gallery) if f.lower().endswith(('.png', '.jpg', '.webp'))])
        else:
            p["gallery_count"] = 0
    return profiles


@router.post("/profiles")
def save_profile(req: ProfileCreateReq):
    profiles = _load_profiles()
    pid = req.id or f"kol_{uuid.uuid4().hex[:8]}"
    existing = next((p for p in profiles if p["id"] == pid), None)
    now = int(time.time())
    item = {
        "id": pid,
        "name": req.name,
        "tagline": req.tagline,
        "age": req.age,
        "archetype": req.archetype,
        "nationality": req.nationality,
        "voice": req.voice or "vi-VN-HoaiMyNeural",
        "dna_prompt": req.dna_prompt,
        "negative_prompt": req.negative_prompt,
        "bio": req.bio,
        "personality_tone": req.personality_tone,
        "updated_at": now,
        "created_at": existing.get("created_at", now) if existing else now,
        "face_anchor_url": existing.get("face_anchor_url", None) if existing else None,
        "gallery_count": existing.get("gallery_count", 0) if existing else 0,
    }
    if existing:
        profiles[profiles.index(existing)] = item
    else:
        profiles.append(item)
    _save_profiles(profiles)
    return item


@router.delete("/profiles/{profile_id}")
def delete_profile(profile_id: str):
    profiles = _load_profiles()
    profiles = [p for p in profiles if p["id"] != profile_id]
    _save_profiles(profiles)
    return {"status": "ok", "deleted": profile_id}


@router.post("/profiles/{profile_id}/anchor")
async def upload_anchor(profile_id: str, file: UploadFile = File(...)):
    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")
    ext = os.path.splitext(file.filename or "")[1].lower() or ".webp"
    filename = f"{profile_id}_anchor{ext}"
    dest = os.path.join(ANCHORS_DIR, filename)
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    anchor_url = f"/kol/media/anchors/{filename}"
    profile["face_anchor_url"] = anchor_url
    _save_profiles(profiles)
    return {"status": "ok", "anchor_url": anchor_url}


@router.post("/generate-image")
async def generate_lookbook_image(req: GenerateImageReq, request: Request):
    from app import CFG, _run_generation, media_url, store

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")

    presets = _load_presets()
    scenes = {s["id"]: s for s in presets.get("lookbook_scenes", [])}
    scene = scenes.get(req.scene_id) if req.scene_id else None

    # Synthesize prompt
    parts = []
    if profile.get("dna_prompt"):
        parts.append(profile["dna_prompt"].strip())
    if scene and scene.get("prompt_addon"):
        parts.append(scene["prompt_addon"].strip())
    if req.custom_prompt:
        parts.append(req.custom_prompt.strip())

    ratio = req.aspect_ratio or (scene.get("best_ratio") if scene else "1:1")
    parts.append(f"【Khung hình và tỉ lệ】: {ratio} aspect ratio")
    parts.append("【Chất lượng】: photorealistic raw color film aesthetic, ultra-sharp 8k, flawless natural skin, beautiful lighting, completely clean without text or watermark")

    final_prompt = "，".join(parts)

    ref_img_path = None
    if req.use_face_anchor and profile.get("face_anchor_url"):
        # Convert relative anchor url to local path or keep reference
        anchor_fn = os.path.basename(profile["face_anchor_url"])
        local_anchor = os.path.join(ANCHORS_DIR, anchor_fn)
        if os.path.exists(local_anchor):
            ref_img_path = local_anchor

    log.info("[KOL] Generating image for %s with prompt: %s (ref: %s)", profile["name"], final_prompt[:80], ref_img_path)

    try:
        res, acc_id = _run_generation(
            final_prompt,
            kind="image",
            timeout=CFG.image_timeout,
            reference_image=ref_img_path,
        )
        url = media_url(res["filename"])

        # Save to profile gallery
        p_gallery = os.path.join(GALLERY_DIR, req.profile_id)
        os.makedirs(p_gallery, exist_ok=True)
        media_src = os.path.join(BASE_DIR, "data", "media", res["filename"])
        if os.path.exists(media_src):
            shutil.copy2(media_src, os.path.join(p_gallery, res["filename"]))

        return {
            "status": "success",
            "url": url,
            "filename": res["filename"],
            "prompt": final_prompt,
            "account": acc_id,
        }
    except Exception as exc:
        log.exception("[KOL] Image generation failed: %s", exc)
        raise HTTPException(500, f"Sinh ảnh thất bại: {exc}") from exc


@router.post("/generate-video")
async def generate_motion_video(req: GenerateVideoReq, request: Request):
    from app import CFG, _run_generation, media_url, store

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")

    presets = _load_presets()
    motions = {m["id"]: m for m in presets.get("motion_presets", [])}
    motion = motions.get(req.motion_id) if req.motion_id else None

    parts = []
    if motion and motion.get("prompt_text"):
        parts.append(motion["prompt_text"].strip())
    if req.custom_motion:
        parts.append(req.custom_motion.strip())
    if not parts:
        parts.append("The girl smiles charmingly at the camera, blinking gently with soft natural movement")

    duration = req.duration or 5
    ratio = req.aspect_ratio or "9:16"
    parts.append(f"video duration {duration} seconds, aspect ratio {ratio}, 4k ultra-smooth lifelike video")

    final_prompt = "，".join(parts)
    ref_img = req.image_url

    # Check if local relative url
    if ref_img.startswith("/v1/media/"):
        fn = os.path.basename(ref_img)
        local_fn = os.path.join(BASE_DIR, "data", "media", fn)
        if os.path.exists(local_fn):
            ref_img = local_fn
    elif ref_img.startswith("/kol/media/"):
        rel = ref_img.replace("/kol/media/", "").replace("/", os.sep)
        local_fn = os.path.join(KOL_DIR, rel)
        if os.path.exists(local_fn):
            ref_img = local_fn

    # Create asynchronous task using existing store
    task = store.create_task("video", f"KOL {profile['name']}: {final_prompt[:60]}")
    store.update_task(task["id"], api_prompt=final_prompt, progress=10)

    import threading

    def worker():
        store.update_task(task["id"], status="processing", progress=15)
        t0 = time.time()
        try:
            def prog_cb(p):
                store.update_task(task["id"], progress=p)
            res, acc_id = _run_generation(
                final_prompt,
                "video",
                CFG.video_timeout,
                on_progress=prog_cb,
                reference_image=ref_img,
            )
            vurl = media_url(res["filename"])
            store.update_task(
                task["id"],
                status="completed",
                progress=100,
                account=acc_id,
                elapsed=round(time.time() - t0, 1),
                url=vurl,
                video={"url": vurl},
                result={"url": vurl, "filename": res["filename"], "bytes": res["size"], "kind": "video"},
            )
            # Save to profile gallery
            p_gallery = os.path.join(GALLERY_DIR, req.profile_id)
            os.makedirs(p_gallery, exist_ok=True)
            media_src = os.path.join(BASE_DIR, "data", "media", res["filename"])
            if os.path.exists(media_src):
                shutil.copy2(media_src, os.path.join(p_gallery, res["filename"]))
        except Exception as exc:
            log.exception("[KOL] Video task %s failed: %s", task["id"], exc)
            store.update_task(task["id"], status="failed", elapsed=round(time.time() - t0, 1), error=str(exc))

    threading.Thread(target=worker, daemon=True).start()
    return {"status": "queued", "task_id": task["id"], "progress": 10}


@router.get("/tasks/{task_id}")
def get_kol_task(task_id: str):
    from app import store
    t = store.get_task(task_id)
    if not t:
        raise HTTPException(404, "Tác vụ không tồn tại")
    out = dict(t)
    status = out.get("status")
    if status in ("succeeded", "success", "done"):
        out["status"] = "completed"
    if out.get("status") == "completed":
        out["progress"] = 100
    elif out.get("status") == "processing":
        elapsed = time.time() - out.get("created_at", time.time())
        calc_prog = min(92, int(20 + elapsed * 1.1))
        out["progress"] = max(out.get("progress", 0) or 0, calc_prog)
    return out


@router.post("/generate-voice")
async def generate_voice(req: VoiceReq):
    text = (req.text or "").strip()
    if not text:
        raise HTTPException(400, "Văn bản lời thoại không được để trống")
    voice_id = req.voice_id or "vi-VN-HoaiMyNeural"
    rate = req.rate or "+0%"
    pitch = req.pitch or "+0Hz"

    audio_id = f"voice_{uuid.uuid4().hex[:10]}.mp3"
    dest_path = os.path.join(AUDIO_DIR, audio_id)

    last_err = None
    for attempt in range(3):
        try:
            if attempt == 0 and (rate != "+0%" or pitch != "+0Hz"):
                c = edge_tts.Communicate(text, voice_id, rate=rate, pitch=pitch)
            else:
                c = edge_tts.Communicate(text, voice_id)
            await c.save(dest_path)
            if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
                return {
                    "status": "ok",
                    "audio_url": f"/kol/media/audio/{audio_id}",
                    "filename": audio_id,
                    "text": text,
                    "voice": voice_id,
                }
        except Exception as exc:
            last_err = exc
            log.warning("[KOL] Voice attempt %d failed: %s, retrying...", attempt, exc)
            await asyncio.sleep(0.5)

    log.exception("[KOL] Voice synthesis error: %s", last_err)
    raise HTTPException(500, f"Tạo giọng nói thất bại: {last_err}") from last_err


@router.post("/mux-media")
async def mux_video_audio(req: MuxReq):
    """Merges a video file and an audio track into a single MP4 with sound using FFmpeg."""
    v_url = req.video_url
    a_url = req.audio_url

    # Resolve local video path
    v_path = None
    if "/v1/media/" in v_url:
        fn = os.path.basename(v_url)
        cand = os.path.join(BASE_DIR, "data", "media", fn)
        if os.path.exists(cand):
            v_path = cand
    elif "/kol/media/" in v_url:
        rel = v_url.split("/kol/media/")[-1].replace("/", os.sep)
        cand = os.path.join(KOL_DIR, rel)
        if os.path.exists(cand):
            v_path = cand

    # Resolve local audio path
    a_path = None
    if "/kol/media/audio/" in a_url:
        fn = os.path.basename(a_url)
        cand = os.path.join(AUDIO_DIR, fn)
        if os.path.exists(cand):
            a_path = cand

    if not v_path or not os.path.exists(v_path):
        raise HTTPException(400, "Không tìm thấy file video trên hệ thống")
    if not a_path or not os.path.exists(a_path):
        raise HTTPException(400, "Không tìm thấy file audio trên hệ thống")

    out_fn = f"muxed_{uuid.uuid4().hex[:10]}.mp4"
    out_path = os.path.join(VIDEOS_DIR, out_fn)

    # ffmpeg -y -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest output.mp4
    cmd = [
        FFMPEG_BIN,
        "-y",
        "-i", v_path,
        "-i", a_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        out_path,
    ]

    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {
            "status": "ok",
            "muxed_url": f"/kol/media/videos/{out_fn}",
            "filename": out_fn,
        }
    except Exception as exc:
        log.exception("[KOL] FFmpeg mux error: %s", exc)
        raise HTTPException(500, f"Ghép video và âm thanh thất bại: {exc}") from exc


@router.post("/generate-caption")
async def generate_caption(req: CaptionReq):
    """Uses muse-spark via safe_chat_stream to generate high-engaging social captions and hashtags."""
    from app import CFG, safe_chat_stream, store

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")

    presets = _load_presets()
    styles = {s["id"]: s for s in presets.get("caption_styles", [])}
    style = styles.get(req.style_id, {"name": "Tự do", "desc": ""})

    sys_prompt = f"""Bạn đang đóng vai là một cô gái KOL ảo nổi tiếng trên mạng xã hội tên là {profile['name']} ({profile['age']} tuổi, {profile['archetype']}).
Tính cách và phong cách: {profile.get('personality_tone') or 'Dễ thương, gần gũi'}
Tiểu sử: {profile.get('bio') or ''}

Nhiệm vụ của bạn: Viết bài đăng mạng xã hội (Facebook/Instagram/TikTok) cho bức ảnh/video mới chụp.
Phong cách bài viết yêu cầu: {style['name']} - {style['desc']}
Chủ đề / bối cảnh cụ thể: {req.scene_name or 'Đời thường'} {req.topic or ''}

Yêu cầu định dạng bài viết:
1. Tiêu đề / Câu Hook thu hút ngay 3 giây đầu tiên (kèm icon sinh động).
2. Thân bài chia sẻ tự nhiên, cảm xúc, đúng giọng điệu của {profile['name']}, xưng hô 'em' hoặc tên mình.
3. Câu hỏi kêu gọi tương tác (Call to action - ví dụ: thả tim, hỏi ý kiến fan).
4. Dòng hashtag trending liên quan (từ 5 - 8 hashtag tiếng Việt và tiếng Anh).

Hãy viết hoàn toàn bằng tiếng Việt tự nhiên, có duyên, không sáo rỗng."""

    prompt = f"{sys_prompt}\n\nNgười dùng: Bối cảnh hôm nay là '{req.scene_name or 'Đi dạo phố'}'. Em hãy viết 1 bài status/caption thật hay và thu hút theo đúng tính cách của em."

    acc = store.pick_account(rotate=True)
    if not acc:
        raise HTTPException(400, "Chưa có tài khoản Muse nào khả dụng trong hệ thống")

    acc_id = acc["id"]
    cookies = acc["cookies"]
    expires = acc.get("cookies_exp")
    timeout = int(CFG.chat_timeout or 120)

    try:
        def run_chat():
            return "".join(safe_chat_stream(cookies, prompt, expires, timeout, account_id=acc_id))
        full_text = await asyncio.to_thread(run_chat)
        return {
            "status": "ok",
            "caption": full_text,
            "character": profile["name"],
            "style": style["name"],
        }
    except Exception as exc:
        log.exception("[KOL] Caption generation error: %s", exc)
        raise HTTPException(500, f"Tạo caption thất bại: {exc}") from exc


@router.get("/gallery/{profile_id}")
def get_gallery(profile_id: str):
    p_gallery = os.path.join(GALLERY_DIR, profile_id)
    if not os.path.exists(p_gallery):
        return []
    items = []
    for fn in os.listdir(p_gallery):
        if fn.lower().endswith(('.png', '.jpg', '.webp', '.mp4')):
            full = os.path.join(p_gallery, fn)
            items.append({
                "filename": fn,
                "url": f"/v1/media/{fn}",
                "kind": "video" if fn.lower().endswith(".mp4") else "image",
                "mtime": int(os.path.getmtime(full)),
                "size": os.path.getsize(full),
            })
    items.sort(key=lambda x: x["mtime"], reverse=True)
    return items
