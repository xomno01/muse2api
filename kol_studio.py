"""MuseKOL Studio — Backend Engine for Virtual AI Influencer Creation & Production.

Integrates Meta Muse image/video/chat models with Edge-TTS voice generation,
FFmpeg media muxing, Face Anchor consistency, and Lookbook presets.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
import shutil
import subprocess
import threading
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
    return {"characters": [], "lookbook_scenes": [], "motion_presets": [], "voices": [], "caption_styles": [], "script_formats": []}


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
    height: Optional[str] = "165 cm"
    weight: Optional[str] = "47 kg"
    body_type: Optional[str] = "slender"
    three_sizes: Optional[str] = "82-59-88"
    skin_tone: Optional[str] = "Trắng hồng tự nhiên"
    voice: Optional[str] = "vi-VN-HoaiMyNeural"
    dna_prompt: str
    negative_prompt: Optional[str] = ""
    bio: Optional[str] = ""
    personality_tone: Optional[str] = ""
    multi_angle_anchors: Optional[dict] = None


class SetAngleAnchorReq(BaseModel):
    profile_id: str
    angle_key: str  # front, three_quarter, profile, full_body
    image_url: Optional[str] = None


class CharacterSheetReq(BaseModel):
    profile_id: str
    aspect_ratio: Optional[str] = "16:9"


class GenerateImageReq(BaseModel):
    profile_id: str
    scene_id: Optional[str] = None
    angle_id: Optional[str] = "angle_front"
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


class ScriptReq(BaseModel):
    profile_id: str
    user_idea: str
    format_id: Optional[str] = "street_interview"
    extra_tone: Optional[str] = ""


class AutoProduceReq(BaseModel):
    profile_id: str
    user_idea: str
    angle_id: Optional[str] = "auto"
    duration: Optional[int] = 5
    aspect_ratio: Optional[str] = "9:16"
    voice_id: Optional[str] = None
    add_subtitles: Optional[bool] = True
    use_face_anchor: Optional[bool] = True


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
        "height": req.height or (existing.get("height") if existing else "165 cm"),
        "weight": req.weight or (existing.get("weight") if existing else "47 kg"),
        "body_type": req.body_type or (existing.get("body_type") if existing else "slender"),
        "three_sizes": req.three_sizes or (existing.get("three_sizes") if existing else "82-59-88"),
        "skin_tone": req.skin_tone or (existing.get("skin_tone") if existing else "Trắng hồng tự nhiên"),
        "voice": req.voice or "vi-VN-HoaiMyNeural",
        "dna_prompt": req.dna_prompt,
        "negative_prompt": req.negative_prompt,
        "bio": req.bio,
        "personality_tone": req.personality_tone,
        "updated_at": now,
        "created_at": existing.get("created_at", now) if existing else now,
        "face_anchor_url": existing.get("face_anchor_url", None) if existing else None,
        "multi_angle_anchors": req.multi_angle_anchors or (existing.get("multi_angle_anchors") if existing else {
            "front": existing.get("face_anchor_url") if existing else None,
            "three_quarter": None,
            "profile": None,
            "full_body": None,
        }),
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
    if "multi_angle_anchors" not in profile or not isinstance(profile["multi_angle_anchors"], dict):
        profile["multi_angle_anchors"] = {}
    profile["multi_angle_anchors"]["front"] = anchor_url
    _save_profiles(profiles)
    return {"status": "ok", "anchor_url": anchor_url}


@router.post("/profiles/{profile_id}/angle-anchor/{angle_key}")
async def upload_angle_anchor(profile_id: str, angle_key: str, file: UploadFile = File(...)):
    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")
    if angle_key not in ("front", "three_quarter", "profile", "full_body"):
        raise HTTPException(400, "Góc không hợp lệ (hỗ trợ: front, three_quarter, profile, full_body)")
    ext = os.path.splitext(file.filename or "")[1].lower() or ".webp"
    filename = f"{profile_id}_{angle_key}{ext}"
    dest = os.path.join(ANCHORS_DIR, filename)
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    anchor_url = f"/kol/media/anchors/{filename}"
    if "multi_angle_anchors" not in profile or not isinstance(profile["multi_angle_anchors"], dict):
        profile["multi_angle_anchors"] = {}
    profile["multi_angle_anchors"][angle_key] = anchor_url
    if angle_key == "front":
        profile["face_anchor_url"] = anchor_url
    _save_profiles(profiles)
    return {"status": "ok", "anchor_url": anchor_url, "angle_key": angle_key, "multi_angle_anchors": profile["multi_angle_anchors"]}


@router.post("/set-angle-anchor")
def set_angle_anchor(req: SetAngleAnchorReq):
    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")
    if req.angle_key not in ("front", "three_quarter", "profile", "full_body"):
        raise HTTPException(400, "Góc không hợp lệ (hỗ trợ: front, three_quarter, profile, full_body)")
    if "multi_angle_anchors" not in profile or not isinstance(profile["multi_angle_anchors"], dict):
        profile["multi_angle_anchors"] = {}
    profile["multi_angle_anchors"][req.angle_key] = req.image_url
    if req.angle_key == "front":
        profile["face_anchor_url"] = req.image_url
    _save_profiles(profiles)
    return {"status": "ok", "multi_angle_anchors": profile["multi_angle_anchors"]}


@router.post("/generate-character-sheet")
async def generate_character_sheet(req: CharacterSheetReq):
    """Tạo bảng mẫu xoay đa hướng 360 độ (Turnaround Model Sheet) để khóa khuôn mặt và vóc dáng nhân vật."""
    from app import CFG, _run_generation, media_url, ImageRequest, build_image_prompt

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")

    presets = _load_presets()
    b_types = {b["id"]: b for b in presets.get("body_types", [])}
    b_info = b_types.get(profile.get("body_type", "slender"))
    b_desc = b_info["prompt_snippet"] if b_info else profile.get("body_type", "slender")

    h = profile.get("height", "165cm")
    w = profile.get("weight", "47kg")
    skin = profile.get("skin_tone", "fair porcelain skin")

    sheet_prompt = f"Character turnaround model sheet of {profile['name']}, {profile.get('dna_prompt', '')}, exact height {h}, weight {w}, {b_desc}, {skin}, displaying 4 distinct angles in a clean multi-view lineup: 1. Full body front view, 2. Three-quarter 45-degree angle view, 3. True 90-degree side profile silhouette, 4. Intimate facial close-up portrait with natural micro-expressions. Same person, identical facial landmarks, consistent casual minimalist outfit, neutral gray studio backdrop, balanced professional lighting, photorealistic 8k, raw color film aesthetic, character design reference sheet, ultra-sharp detail"

    img_req = ImageRequest(
        prompt=sheet_prompt,
        aspect_ratio=req.aspect_ratio or "16:9",
        reference_image=None
    )
    api_prompt = build_image_prompt(img_req)

    try:
        res, acc_id = _run_generation(
            api_prompt,
            kind="image",
            timeout=CFG.image_timeout,
            reference_image=None
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
            "prompt": sheet_prompt,
            "account": acc_id
        }
    except Exception as exc:
        log.exception("[KOL] Character sheet generation error: %s", exc)
        raise HTTPException(500, f"Tạo bảng mẫu đa hướng thất bại: {exc}") from exc


@router.post("/generate-image")
async def generate_lookbook_image(req: GenerateImageReq, request: Request):
    from app import CFG, _run_generation, media_url, store, ImageRequest, build_image_prompt

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")

    presets = _load_presets()
    scenes = {s["id"]: s for s in presets.get("lookbook_scenes", [])}
    scene = scenes.get(req.scene_id) if req.scene_id else None
    angles = {a["id"]: a for a in presets.get("camera_angles", [])}
    angle = angles.get(req.angle_id) if req.angle_id else None

    b_types = {b["id"]: b for b in presets.get("body_types", [])}
    b_info = b_types.get(profile.get("body_type", "slender"))
    b_desc = b_info["prompt_snippet"] if b_info else profile.get("body_type", "slender")

    # Synthesize prompt with full biometric & angle consistency
    parts = []
    if profile.get("dna_prompt"):
        parts.append(profile["dna_prompt"].strip())

    # Biometrics: height, weight, body_type, skin
    bio_specs = []
    if profile.get("height"):
        bio_specs.append(f"height {profile['height']}")
    if profile.get("weight"):
        bio_specs.append(f"weight {profile['weight']}")
    if b_desc:
        bio_specs.append(b_desc)
    if profile.get("three_sizes"):
        bio_specs.append(f"body measurements {profile['three_sizes']}")
    if profile.get("skin_tone"):
        bio_specs.append(profile["skin_tone"])
    if bio_specs:
        parts.append(", ".join(bio_specs))

    # Angle & Perspective
    if angle and angle.get("prompt_addon"):
        parts.append(angle["prompt_addon"].strip())

    # Scene
    if scene and scene.get("prompt_addon"):
        parts.append(scene["prompt_addon"].strip())
    if req.custom_prompt:
        parts.append(req.custom_prompt.strip())

    ratio = req.aspect_ratio or (angle.get("best_ratio") if angle else (scene.get("best_ratio") if scene else "1:1"))

    combined_prompt = "，".join(parts)
    img_req = ImageRequest(
        prompt=combined_prompt,
        aspect_ratio=ratio,
        reference_image=None
    )
    final_prompt = build_image_prompt(img_req)

    ref_img_path = None
    if req.use_face_anchor and profile.get("face_anchor_url"):
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


@router.post("/generate-script")
async def generate_script(req: ScriptReq):
    """Uses muse-spark via safe_chat_stream to generate full viral short video scripts with scenes, dialogues, lookbook prompt, and voiceover text."""
    from app import CFG, safe_chat_stream, store

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")

    presets = _load_presets()
    formats = {f["id"]: f for f in presets.get("script_formats", [])}
    fmt = formats.get(req.format_id, {
        "name": "Phỏng vấn đường phố hài hước",
        "desc": "KOL cầm micro hoặc đạo cụ phỏng vấn người dân tại hiện trường với các câu hỏi bất ngờ, đối đáp hài hước."
    })

    idea = req.user_idea.strip()
    if not idea:
        raise HTTPException(400, "Vui lòng nhập ý tưởng kịch bản")

    extra_tone = req.extra_tone.strip() or "Hài hước, dí dỏm, biểu cảm phong phú, dùng tiếng lóng tự nhiên đời thường của giới trẻ Việt Nam"
    dna_summary = profile.get("dna_prompt", "")[:220]

    sys_prompt = f"""Bạn là Đạo diễn kiêm Biên kịch hàng đầu cho các kênh TikTok/Reels triệu view của các Virtual KOL (KOL Ảo).
Nhân vật chính của kịch bản là bé KOL tên: {profile['name']} ({profile.get('age', 21)} tuổi, {profile.get('archetype', 'Nàng thơ')}, quốc tịch {profile.get('nationality', 'Việt Nam')}).
Tính cách nhân vật: {profile.get('personality_tone') or 'Hài hước, duyên dáng, gần gũi'}
DNA ngoại hình của {profile['name']}: {dna_summary}

Thể loại video: {fmt['name']} ({fmt['desc']})
Ý tưởng kịch bản từ người dùng: "{idea}"
Yêu cầu phong cách bổ sung: {extra_tone}

HÃY DỰNG MỘT KỊCH BẢN VIDEO VIRAL HOÀN CHỈNH (thời lượng 30s - 60s, chia làm 4 cảnh) theo ĐÚNG cấu trúc sau:

# 🎬 KỊCH BẢN: [Đặt tiêu đề giật tít, siêu bắt tai, hài hước]
**Nhân vật chính:** {profile['name']}
**Thể loại:** {fmt['name']}
**Bối cảnh:** [Mô tả ngắn gọn không gian hiện trường]
**Hook 3 giây đầu:** [Câu nói hoặc hành động bất ngờ mở màn giật spotlight ngay lập tức]

---

### 🎭 PHÂN CẢNH CHI TIẾT

#### 🎬 CẢNH 1: Mở Màn - Hiện Trường & Cú Hook (3-5s)
- **Hành động & Biểu cảm KOL:** [Mô tả cụ thể nét mặt hài hước, cử chỉ lầy lội, đạo cụ cầm trên tay]
- **Lời thoại KOL:** "[Lời thoại mở màn hài hước chào khán giả]"
- **📸 Lookbook Prompt (English):** [1 câu prompt tiếng Anh chi tiết để tạo ảnh bìa/ảnh cảnh 1 chất lượng photorealistic 8k, gắn với {profile['name']}, bối cảnh hiện trường, biểu cảm hài hước, không chứa chữ]
- **🎙️ Voiceover (Cảnh 1):** [Lời thoại ngắn]

#### 🎬 CẢNH 2: Phỏng Vấn Người Dân 1 / Tình Huống Éo Le Thứ Nhất (5-8s)
- **Nhân vật tương tác:** [Mô tả người dân được phỏng vấn, trang phục, dáng vẻ ngộ nghĩnh]
- **Hành động:** [KOL tiến lại gần, biểu cảm dở khóc dở cười]
- **Đối thoại Phỏng vấn (Hài hước khó đỡ):**
  - **{profile['name']}:** "[Câu hỏi phỏng vấn bất ngờ, lầy lội]"
  - **Người dân:** "[Câu trả lời thật thà ngô nghê hoặc 'bá đạo' khiến ai nghe cũng bật cười]"
- **📸 Lookbook Prompt (English):** [Prompt tiếng Anh mô tả cảnh tương tác này]

#### 🎬 CẢNH 3: Phỏng Vấn Người Dân 2 / Tình Huống Cao Trào (5-8s)
- **Nhân vật tương tác:** [Nhân vật thứ 2 cá tính hoặc tình huống bất ngờ ập tới]
- **Hành động:** [Pha xử lý hài hước không đụng hàng]
- **Đối thoại Phỏng vấn (Cười ra nước mắt):**
  - **{profile['name']}:** "[Câu hỏi hoặc nhận xét hài hước]"
  - **Người dân:** "[Pha đối đáp lầy lội, chốt hạ ấn tượng]"
- **📸 Lookbook Prompt (English):** [Prompt tiếng Anh mô tả cảnh này]

#### 🎬 CẢNH 4: Pha Chốt Hạ & Kêu Gọi Tương Tác (Outro) (3-5s)
- **Hành động & Biểu cảm KOL:** [Biểu cảm 'bất lực' hài hước hoặc tạo dáng dễ thương chào tạm biệt]
- **Lời thoại kết:** "[Câu chốt duyên dáng, hỏi ý kiến khán giả và kêu gọi follow]"
- **🎙️ Voiceover (Cảnh 4):** [Lời thoại kết]

---

### 🎙️ TOÀN BỘ LỜI THOẠI LỒNG TIẾNG (EDGE-TTS READY)
[Viết liền mạch toàn bộ các câu nói của {profile['name']} từ Cảnh 1 đến Cảnh 4 để người dùng copy trực tiếp vào Phòng Thu Voice Studio tạo giọng đọc liền một mạch]

---

### 📸 LOOKBOOK PROMPT CHÍNH (LOOKBOOK STUDIO READY)
[Viết 1 đoạn prompt tiếng Anh hoàn chỉnh kết hợp DNA ngoại hình của {profile['name']} và bối cảnh đắt giá nhất của clip, chuẩn bị sẵn sàng để paste vào Xưởng Chụp Lookbook Studio tạo ảnh 8K]

---

### 📱 STATUS & HASHTAG ĐĂNG MẠNG XÃ HỘI
[Viết 1 status ngắn gọn cực hút kèm 6-8 hashtag thịnh hành TikTok/Facebook/Reels]

Hãy viết với lời thoại tự nhiên nhất, dùng từ ngữ đời sống phong phú, hài hước hóm hỉnh, tuyệt đối không giáo điều sáo rỗng!"""

    acc = store.pick_account(rotate=True)
    if not acc:
        raise HTTPException(400, "Chưa có tài khoản Muse nào khả dụng trong hệ thống")

    acc_id = acc["id"]
    cookies = acc["cookies"]
    expires = acc.get("cookies_exp")
    timeout = int(CFG.chat_timeout or 120)

    try:
        def run_chat():
            return "".join(safe_chat_stream(cookies, sys_prompt, expires, timeout, account_id=acc_id))
        full_text = await asyncio.to_thread(run_chat)

        import re
        extracted_lookbook = ""
        lb_match = re.search(r"(?:###\s*)?📸\s*LOOKBOOK PROMPT CHÍNH[^\n]*\n+([\s\S]*?)(?=(?:\n+(?:###\s*)?[📸🎙️📱])|\Z)", full_text, re.IGNORECASE)
        if lb_match:
            extracted_lookbook = lb_match.group(1).strip("` \n\r")
        if not extracted_lookbook:
            sc_match = re.search(r"📸\s*Lookbook Prompt \(English\):\s*`?([^\n`]+)`?", full_text, re.IGNORECASE)
            if sc_match:
                extracted_lookbook = sc_match.group(1).strip()
        if not extracted_lookbook:
            extracted_lookbook = f"{profile.get('dna_prompt', '')}, funny street moment, {idea}, photorealistic 8k"

        extracted_voice = ""
        vc_match = re.search(r"(?:###\s*)?🎙️\s*TOÀN BỘ LỜI THOẠI LỒNG TIẾNG[^\n]*\n+([\s\S]*?)(?=(?:\n+(?:###\s*)?[📸🎙️📱])|\Z)", full_text, re.IGNORECASE)
        if vc_match:
            extracted_voice = vc_match.group(1).strip("` \n\r")
        if not extracted_voice:
            dial_matches = re.findall(rf"(?:{re.escape(profile['name'])}|KOL):\s*\"([^\"]+)\"", full_text)
            if dial_matches:
                # Deduplicate consecutive duplicates
                dedup = []
                for d in dial_matches:
                    if not dedup or dedup[-1] != d:
                        dedup.append(d)
                extracted_voice = " ".join(dedup)

        return {
            "status": "ok",
            "script": full_text,
            "character": profile["name"],
            "format": fmt["name"],
            "lookbook_prompt": extracted_lookbook,
            "voice_text": extracted_voice,
        }
    except Exception as exc:
        log.exception("[KOL] Script generation error: %s", exc)
        raise HTTPException(500, f"Dựng kịch bản thất bại: {exc}") from exc


@router.get("/gallery/{profile_id}")
def get_gallery(profile_id: str):
    p_gallery = os.path.join(GALLERY_DIR, profile_id)
    if not os.path.exists(p_gallery):
        return []
    items = []
    for fn in os.listdir(p_gallery):
        if fn.lower().endswith(('.png', '.jpg', '.webp', '.mp4')):
            full = os.path.join(p_gallery, fn)
            if os.path.exists(os.path.join(VIDEOS_DIR, fn)):
                item_url = f"/kol/media/videos/{fn}"
            elif os.path.exists(os.path.join(ANCHORS_DIR, fn)):
                item_url = f"/kol/media/anchors/{fn}"
            elif os.path.exists(os.path.join(BASE_DIR, "data", "media", fn)):
                item_url = f"/v1/media/{fn}"
            else:
                item_url = f"/kol/media/gallery/{profile_id}/{fn}"

            items.append({
                "filename": fn,
                "url": item_url,
                "kind": "video" if fn.lower().endswith(".mp4") else "image",
                "mtime": int(os.path.getmtime(full)),
                "size": os.path.getsize(full),
            })
    items.sort(key=lambda x: x["mtime"], reverse=True)
    return items


# ===================== Auto Video Production Engine =====================
AUTO_TASKS: dict[str, dict] = {}


def _get_media_duration(file_path: str) -> float:
    cmd = [FFMPEG_BIN, "-i", file_path]
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", p.stderr)
        if m:
            hours, mins, secs = float(m.group(1)), float(m.group(2)), float(m.group(3))
            return hours * 3600 + mins * 60 + secs
    except Exception as e:
        log.warning("Failed to get duration of %s: %s", file_path, e)
    return 5.0


def _generate_srt_file(text: str, total_duration: float, srt_dest_path: str):
    clean_text = text.replace("\n", " ").strip()
    raw_parts = [p.strip() for p in re.split(r"([.!?…,:;]+)", clean_text) if p.strip()]
    lines = []
    i = 0
    while i < len(raw_parts):
        chunk = raw_parts[i]
        if i + 1 < len(raw_parts) and re.match(r"^[.!?…,:;]+$", raw_parts[i+1]):
            chunk += raw_parts[i+1]
            i += 2
        else:
            i += 1
        if len(chunk) > 2:
            lines.append(chunk)

    if not lines:
        lines = [clean_text]

    merged = []
    buf = ""
    for l in lines:
        buf = (buf + " " + l).strip()
        if len(buf.split()) >= 6:
            merged.append(buf)
            buf = ""
    if buf:
        merged.append(buf)
    lines = merged or lines

    count = len(lines)
    time_per_line = max(1.0, total_duration / count)

    def format_ts(sec: float) -> str:
        hours = int(sec // 3600)
        mins = int((sec % 3600) // 60)
        secs = int(sec % 60)
        millis = int((sec - int(sec)) * 1000)
        return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

    srt_entries = []
    for idx, line in enumerate(lines):
        start_sec = idx * time_per_line
        end_sec = min(total_duration, (idx + 1) * time_per_line)
        srt_entries.append(f"{idx + 1}\n{format_ts(start_sec)} --> {format_ts(end_sec)}\n{line}\n")

    with open(srt_dest_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))


def _mux_with_subtitles(v_path: str, a_path: str, srt_path: Optional[str], out_path: str):
    vf_filter = None
    if srt_path and os.path.exists(srt_path):
        srt_esc = os.path.abspath(srt_path).replace("\\", "/")
        if ":" in srt_esc:
            d, r = srt_esc.split(":", 1)
            srt_esc = f"{d}\\:{r}"
        vf_filter = f"subtitles='{srt_esc}':force_style='FontSize=22,Fontname=Arial,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=3,Outline=2,Alignment=2,MarginV=50'"

    cmd = [
        FFMPEG_BIN, "-y",
        "-stream_loop", "-1",
        "-i", v_path,
        "-i", a_path,
        "-map", "0:v:0",
        "-map", "1:a:0",
    ]
    if vf_filter:
        cmd.extend(["-vf", vf_filter])
    cmd.extend([
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-c:a", "aac",
        "-shortest",
        out_path
    ])

    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
    except Exception as exc:
        log.warning("[KOL] FFmpeg mux with sub failed, retrying without sub: %s", exc)
        cmd_fallback = [
            FFMPEG_BIN, "-y",
            "-stream_loop", "-1",
            "-i", v_path,
            "-i", a_path,
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-c:a", "aac",
            "-shortest",
            out_path
        ]
        subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def _run_auto_produce_worker(task_id: str, req: AutoProduceReq):
    import threading
    from app import CFG, _run_generation, media_url, safe_chat_stream, store

    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        AUTO_TASKS[task_id] = {"status": "failed", "error": "Không tìm thấy hồ sơ KOL", "progress": 0}
        return

    try:
        # Phase 1: Script, Hook, Prompts
        AUTO_TASKS[task_id].update({
            "status": "processing",
            "progress": 15,
            "phase": "1/5",
            "step": "Muse Spark đang sáng tạo kịch bản, câu thoại & prompt bối cảnh...",
        })

        acc = store.pick_account(rotate=True)
        if not acc:
            raise RuntimeError("Chưa có tài khoản Muse nào khả dụng")

        h = profile.get("height", "165 cm")
        w = profile.get("weight", "47 kg")
        b_type = profile.get("body_type", "slender")
        sizes = profile.get("three_sizes", "82-59-88")
        skin = profile.get("skin_tone", "Trắng hồng tự nhiên")
        biometrics_desc = f"Chiều cao: {h}, Cân nặng: {w}, Vóc dáng: {b_type}, Số đo: {sizes}, Da: {skin}"

        prompt = f"""Bạn là Giám đốc Sáng tạo chuyên sản xuất Short Video / Reel TikTok triệu view cho KOL Ảo.
Nhân vật: {profile['name']} ({profile.get('age', 21)} tuổi, {profile.get('archetype', 'Nàng thơ')}).
Thông số nhân trắc học & vóc dáng: {biometrics_desc}
Tính cách: {profile.get('personality_tone', 'Hài hước, duyên dáng')}
DNA ngoại hình: {profile.get('dna_prompt', '')[:220]}

Tình huống người dùng yêu cầu: "{req.user_idea}"

HÃY XUẤT RA CHÍNH XÁC 5 PHẦN THEO ĐÚNG CÚ PHÁP ĐÁNH DẤU SAU (KHÔNG THÊM BỚT):

[TIÊU ĐỀ]
(Tiêu đề ngắn cực cuốn giật tít)

[CÂU THOẠI LỒNG TIẾNG]
(Viết 1 đoạn thoại ngắn khoảng 15-28 từ để bé KOL tự nói, giọng điệu hài hước, lầy lội, tự nhiên đời thường, thích hợp cho clip 5s - 10s)

[LOOKBOOK PROMPT TIẾNG ANH]
(1 đoạn prompt tiếng Anh chi tiết chuẩn 8k photorealistic miêu tả bé {profile['name']} với nét mặt hài hước dở khóc dở cười tại bối cảnh tình huống trên, có giữ chuẩn vóc dáng {h} {w} {b_type} và đặc điểm gương mặt DNA của bé, không chứa chữ)

[MOTION PROMPT TIẾNG ANH]
(1 câu prompt tiếng Anh mô tả cử động khuôn mặt, nói chuyện tự nhiên vào micro/camera, chớp mắt, biểu cảm sống động)

[CAPTION MẠNG XÃ HỘI]
(Status ngắn hài hước kèm 5 hashtag trending)"""

        try:
            resp = "".join(safe_chat_stream(acc['cookies'], prompt, acc.get('cookies_exp'), 120, account_id=acc['id']))
        except Exception as chat_err:
            log.warning("[KOL] Muse chat stream timeout or error: %s. Using high-engaging fallback generator.", chat_err)
            resp = f"""[TIÊU ĐỀ]
Cùng {profile['name']} tác nghiệp thực tế: {req.user_idea[:40]}

[CÂU THOẠI LỒNG TIẾNG]
Trời ơi cả nhà ơi! Hôm nay em đi thực tế mà cười ra nước mắt luôn á, ai cũng nhìn em quá trời!

[LOOKBOOK PROMPT TIẾNG ANH]
{profile.get('dna_prompt', '')}, height {h}, weight {w}, {b_type}, expressive humorous funny facial expression, {req.user_idea}, 8k photorealistic, raw color film aesthetic, ultra-sharp 8k, flawless natural skin, beautiful cinematic lighting, clean without text

[MOTION PROMPT TIẾNG ANH]
The girl speaks naturally into the camera, smiling humorously, lively natural blinking and cute facial expressions, 4k ultra-smooth lifelike video

[CAPTION MẠNG XÃ HỘI]
Hôm nay đi thực tế mà hài hước không đỡ nổi luôn cả nhà ơi 🤣 #{profile['name']} #xuhuong #haihuoc #viral"""

        title_m = re.search(r"\[TIÊU ĐỀ\]\s*\n+([^\n\[]+)", resp)
        title = title_m.group(1).strip() if title_m else f"Clip {profile['name']}: {req.user_idea[:30]}"

        voice_m = re.search(r"\[CÂU THOẠI LỒNG TIẾNG\]\s*\n+([^\n\[]+(?:\n+[^\n\[]+)*)", resp)
        voice_text = voice_m.group(1).strip() if voice_m else f"Chào cả nhà, hôm nay cùng {profile['name']} trải nghiệm nhé!"
        voice_text = voice_text.replace('"', '').replace('“', '').replace('”', '').strip()

        lb_m = re.search(r"\[LOOKBOOK PROMPT TIẾNG ANH\]\s*\n+([\s\S]*?)(?=\n*\[|\n*MOTION PROMPT|\Z)", resp, re.IGNORECASE)
        lookbook_prompt = lb_m.group(1).strip("` \n\r") if lb_m else f"{profile.get('dna_prompt', '')}, in funny situation, {req.user_idea}, 8k photorealistic"
        lookbook_prompt = re.sub(r"^`+|`+$", "", lookbook_prompt).strip()

        motion_m = re.search(r"\[MOTION PROMPT TIẾNG ANH\]\s*\n+([\s\S]*?)(?=\n*\[|\n*CAPTION|\Z)", resp, re.IGNORECASE)
        motion_prompt = motion_m.group(1).strip("` \n\r") if motion_m else "The girl speaks naturally into the camera, smiling humorously, natural blinking and head movement"
        motion_prompt = re.sub(r"^`+|`+$", "", motion_prompt).strip()

        cap_m = re.search(r"\[CAPTION MẠNG XÃ HỘI\]\s*\n+([\s\S]*?)(?=\Z)", resp, re.IGNORECASE)
        caption = cap_m.group(1).strip("` \n\r") if cap_m else f"{title} #{profile['name']} #xuhuong"

        # Phase 2: Lookbook Image / Visual Anchor
        AUTO_TASKS[task_id].update({
            "progress": 35,
            "phase": "2/5",
            "step": f"Đã có kịch bản! Đang chuẩn bị hình ảnh hiện trường cho {profile['name']}...",
            "title": title,
            "voice_text": voice_text,
            "lookbook_prompt": lookbook_prompt,
            "motion_prompt": motion_prompt,
            "caption": caption,
        })

        from app import ImageRequest, build_image_prompt, VideoRequest, build_video_prompt

        p_gallery = os.path.join(GALLERY_DIR, req.profile_id)
        os.makedirs(p_gallery, exist_ok=True)

        img_fn = None
        img_url = None
        img_local = None

        # Resolve base visual anchor if available (prefer front/face anchor)
        anchors_map = profile.get("multi_angle_anchors") or {}
        preferred_anchor_url = anchors_map.get("front") or profile.get("face_anchor_url")
        if req.use_face_anchor and preferred_anchor_url:
            anchor_fn = os.path.basename(preferred_anchor_url)
            cand = os.path.join(ANCHORS_DIR, anchor_fn)
            if os.path.exists(cand):
                img_fn = anchor_fn
                img_url = preferred_anchor_url
                img_local = cand

        # Try generating fresh lookbook image; if Meta image API is temporarily down, use visual anchor
        try:
            dna = profile.get("dna_prompt", "").strip()
            bio_anchor = f"height {h}, weight {w}, {b_type} silhouette"
            combined_prompt = lookbook_prompt
            if bio_anchor.lower() not in lookbook_prompt.lower():
                combined_prompt = f"{combined_prompt}, {bio_anchor}"
            if dna and dna.lower() not in lookbook_prompt.lower():
                combined_prompt = f"{dna}, {combined_prompt}"

            img_req = ImageRequest(
                prompt=combined_prompt,
                aspect_ratio=req.aspect_ratio or "9:16",
                reference_image=None,
            )
            final_img_prompt = build_image_prompt(img_req)

            img_res, img_acc = _run_generation(
                final_img_prompt,
                kind="image",
                timeout=min(CFG.image_timeout, 90),
                reference_image=None,
            )
            img_fn = img_res["filename"]
            img_url = media_url(img_fn)
            img_local = os.path.join(BASE_DIR, "data", "media", img_fn)
            if os.path.exists(img_local):
                shutil.copy2(img_local, os.path.join(p_gallery, img_fn))
        except Exception as img_err:
            log.warning("[KOL] Fresh lookbook image generation bypassed (%s). Using character visual anchor: %s", img_err, img_local)
            if not img_local and preferred_anchor_url:
                anchor_fn = os.path.basename(preferred_anchor_url)
                cand = os.path.join(ANCHORS_DIR, anchor_fn)
                if os.path.exists(cand):
                    img_fn = anchor_fn
                    img_url = preferred_anchor_url
                    img_local = cand

        # Phase 3: Motion Video Generation
        AUTO_TASKS[task_id].update({
            "progress": 55,
            "phase": "3/5",
            "step": f"Đã có ảnh nhân vật! Đang dựng video chuyển động {req.aspect_ratio or '9:16'}...",
            "preview_image": img_url,
        })

        duration = req.duration or 5
        ratio = req.aspect_ratio or "9:16"
        video_instruction = f"{profile['name']} (height {h}, weight {w}, {b_type}), {motion_prompt}"

        vid_req = VideoRequest(
            prompt=video_instruction,
            aspect_ratio=ratio,
            duration=duration,
            reference_image=img_local,
        )
        final_video_prompt = build_video_prompt(vid_req)

        vid_res, vid_acc = _run_generation(
            final_video_prompt,
            kind="video",
            timeout=CFG.video_timeout,
            reference_image=img_local,
        )
        raw_vid_fn = vid_res["filename"]
        raw_vid_url = media_url(raw_vid_fn)
        raw_vid_local = os.path.join(BASE_DIR, "data", "media", raw_vid_fn)

        if os.path.exists(raw_vid_local):
            shutil.copy2(raw_vid_local, os.path.join(p_gallery, raw_vid_fn))

        # Phase 4: Voice Synthesis (Edge-TTS)
        AUTO_TASKS[task_id].update({
            "progress": 80,
            "phase": "4/5",
            "step": "Đã dựng xong video! Đang thu âm giọng đọc AI tiếng Việt...",
            "preview_video": raw_vid_url,
        })

        voice_id = req.voice_id or profile.get("voice", "vi-VN-HoaiMyNeural")
        audio_fn = f"autoprod_{task_id}.mp3"
        audio_path = os.path.join(AUDIO_DIR, audio_fn)

        comm = edge_tts.Communicate(voice_text, voice_id, rate="+0%", pitch="+0Hz")
        asyncio.run(comm.save(audio_path))
        audio_url = f"/kol/media/audio/{audio_fn}"
        audio_dur = _get_media_duration(audio_path)

        # Phase 5: FFmpeg Mux + Subtitles
        AUTO_TASKS[task_id].update({
            "progress": 90,
            "phase": "5/5",
            "step": "Đang ghép âm thanh, video & phụ đề (FFmpeg)...",
            "preview_audio": audio_url,
        })

        final_fn = f"autoprod_{task_id}.mp4"
        final_path = os.path.join(VIDEOS_DIR, final_fn)

        srt_path = None
        if req.add_subtitles:
            srt_fn = f"autoprod_{task_id}.srt"
            srt_path = os.path.join(AUDIO_DIR, srt_fn)
            _generate_srt_file(voice_text, audio_dur, srt_path)

        _mux_with_subtitles(raw_vid_local, audio_path, srt_path, final_path)
        final_url = f"/kol/media/videos/{final_fn}"

        if os.path.exists(final_path):
            shutil.copy2(final_path, os.path.join(p_gallery, final_fn))

        AUTO_TASKS[task_id].update({
            "status": "completed",
            "progress": 100,
            "phase": "5/5",
            "step": "🎉 Hoàn tất! Video thành phẩm đã sẵn sàng phát.",
            "result": {
                "final_video_url": final_url,
                "image_url": img_url,
                "raw_video_url": raw_vid_url,
                "audio_url": audio_url,
                "title": title,
                "voice_text": voice_text,
                "caption": caption,
                "character": profile["name"],
                "audio_duration": round(audio_dur, 1),
            }
        })
        log.info("[KOL] Auto production %s completed successfully: %s", task_id, final_url)

    except Exception as exc:
        log.exception("[KOL] Auto production %s failed: %s", task_id, exc)
        AUTO_TASKS[task_id].update({
            "status": "failed",
            "progress": 0,
            "error": str(exc),
            "step": f"Thất bại: {exc}",
        })


@router.post("/auto-produce")
async def start_auto_produce(req: AutoProduceReq):
    profiles = _load_profiles()
    profile = next((p for p in profiles if p["id"] == req.profile_id), None)
    if not profile:
        raise HTTPException(404, "Không tìm thấy hồ sơ KOL")
    if not req.user_idea.strip():
        raise HTTPException(400, "Vui lòng nhập ý tưởng tình huống")

    task_id = f"auto_{uuid.uuid4().hex[:10]}"
    AUTO_TASKS[task_id] = {
        "id": task_id,
        "status": "processing",
        "progress": 10,
        "phase": "0/5",
        "step": "Đang khởi tạo chu trình sản xuất video trọn gói...",
        "created_at": int(time.time()),
        "profile_id": req.profile_id,
        "user_idea": req.user_idea,
        "result": None,
        "error": None,
        "preview_image": None,
        "preview_video": None,
        "preview_audio": None,
    }

    import threading
    threading.Thread(target=_run_auto_produce_worker, args=(task_id, req), daemon=True).start()
    return {"status": "queued", "task_id": task_id, "progress": 10}


@router.get("/auto-tasks/{task_id}")
def get_auto_produce_task(task_id: str):
    task = AUTO_TASKS.get(task_id)
    if not task:
        raise HTTPException(404, "Không tìm thấy tác vụ sản xuất")
    return task
