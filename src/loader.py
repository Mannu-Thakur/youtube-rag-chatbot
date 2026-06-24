import json
import time
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi

CACHE_DIR = Path("data/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def extract_video_id(video_input: str) -> str:
    value = video_input.strip()

    if "youtube.com" in value or "youtu.be" in value:
        parsed = urlparse(value)

        if parsed.hostname and "youtu.be" in parsed.hostname:
            return parsed.path.strip("/")

        query = parse_qs(parsed.query)
        if "v" in query and query["v"]:
            return query["v"][0]

        if parsed.path:
            return parsed.path.rstrip("/").split("/")[-1]

    return value


def _cache_path(video_id: str) -> Path:
    return CACHE_DIR / f"{video_id}.json"


def load_transcript(video_input: str, languages=("en", "hi"), retries: int = 3):
    video_id = extract_video_id(video_input)
    cache_file = _cache_path(video_id)

    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    api = YouTubeTranscriptApi()
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            transcript = api.fetch(video_id, languages=list(languages))
            segments = [
                {
                    "text": snippet.text,
                    "start": float(snippet.start),
                    "duration": float(snippet.duration),
                }
                for snippet in list(transcript)
            ]

            payload = {
                "video_id": video_id,
                "source_url": f"https://www.youtube.com/watch?v={video_id}",
                "segments": segments,
            }

            cache_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            return payload

        except Exception as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(2 * attempt)

    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    raise RuntimeError(f"Failed to fetch transcript for {video_id}") from last_error


def load_transcripts(video_inputs):
    transcripts = []
    for video_input in video_inputs:
        transcripts.append(load_transcript(video_input))
    return transcripts