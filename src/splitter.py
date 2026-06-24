from langchain_core.documents import Document


def format_seconds(seconds: float) -> str:
    total = max(0, int(seconds))
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

    return f"{minutes:02d}:{secs:02d}"


def _make_chunk_document(video_id: str, source_url: str, chunk_index: int, segments: list[dict]) -> Document:
    texts = [seg["text"].strip() for seg in segments if seg["text"].strip()]
    start_seconds = float(segments[0]["start"])
    end_seconds = float(segments[-1]["start"] + segments[-1]["duration"])

    return Document(
        page_content=" ".join(texts),
        metadata={
            "video_id": video_id,
            "source_url": source_url,
            "chunk_index": chunk_index,
            "start_seconds": start_seconds,
            "end_seconds": end_seconds,
            "time_range": f"{format_seconds(start_seconds)} - {format_seconds(end_seconds)}",
        },
    )


def split_text(transcripts, chunk_size: int = 1000, overlap_segments: int = 2):
    documents = []

    for transcript in transcripts:
        video_id = transcript["video_id"]
        source_url = transcript["source_url"]
        segments = transcript["segments"]

        buffer = []
        buffer_chars = 0
        chunk_index = 0

        for segment in segments:
            text = segment["text"].strip()
            if not text:
                continue

            projected = buffer_chars + len(text) + 1
            if buffer and projected > chunk_size:
                documents.append(
                    _make_chunk_document(video_id, source_url, chunk_index, buffer)
                )
                chunk_index += 1

                if overlap_segments > 0:
                    buffer = buffer[-overlap_segments:]
                    buffer_chars = sum(len(item["text"].strip()) + 1 for item in buffer)
                else:
                    buffer = []
                    buffer_chars = 0

            buffer.append(segment)
            buffer_chars += len(text) + 1

        if buffer:
            documents.append(
                _make_chunk_document(video_id, source_url, chunk_index, buffer)
            )

    return documents