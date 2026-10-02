import requests
import time
import sys

base = "http://127.0.0.1:18610"
payload = {
    "profile_id": "char_linh_dan",
    "user_idea": "kol vẻ mặt hài hước đi phỏng vấn người dân giữa đường ngập nước sau đêm mưa rất lớn tối nay",
    "duration": 5,
    "aspect_ratio": "9:16",
    "add_subtitles": True,
    "use_face_anchor": True
}

print("Triggering 1-Click Auto Production...")
r = requests.post(f"{base}/kol/api/auto-produce", json=payload, timeout=30)
print("Trigger status:", r.status_code, r.text)

if r.status_code != 200:
    sys.exit(1)

task_id = r.json()["task_id"]
print(f"Polling task: {task_id}...")

last_step = ""
while True:
    time.sleep(3)
    t = requests.get(f"{base}/kol/api/auto-tasks/{task_id}").json()
    status = t.get("status")
    prog = t.get("progress", 0)
    step = t.get("step", "")
    phase = t.get("phase", "")

    if step != last_step:
        print(f"[{phase}] ({prog}%) {step}")
        last_step = step

    if status == "completed":
        print("\n=== AUTO PRODUCTION SUCCESSFUL ===")
        res = t.get("result", {})
        print(f"Title: {res.get('title')}")
        print(f"Final Video: {res.get('final_video_url')}")
        print(f"Voice Text: {res.get('voice_text')}")
        print(f"Caption: {res.get('caption')}")
        break
    elif status == "failed":
        print("\n=== AUTO PRODUCTION FAILED ===")
        print("Error:", t.get("error"))
        break
