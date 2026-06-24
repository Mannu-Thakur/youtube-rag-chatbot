import json
from pathlib import Path

from langchain_community.vectorstores import FAISS

INDEX_DIR = Path("faiss_index")
MANIFEST_FILE = INDEX_DIR / "manifest.json"
FAISS_FILE = INDEX_DIR / "index.faiss"
PICKLE_FILE = INDEX_DIR / "index.pkl"


def _normalize_ids(video_ids):
    return sorted(set(video_ids))


def vectorstore_exists(expected_video_ids=None) -> bool:
    if not (FAISS_FILE.exists() and PICKLE_FILE.exists()):
        return False

    if expected_video_ids is None:
        return True

    if not MANIFEST_FILE.exists():
        return False

    try:
        manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    except Exception:
        return False

    saved = _normalize_ids(manifest.get("video_ids", []))
    expected = _normalize_ids(expected_video_ids)
    return saved == expected


def create_vectorstore(documents, embeddings, video_ids):
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(str(INDEX_DIR))

    MANIFEST_FILE.write_text(
        json.dumps(
            {
                "video_ids": _normalize_ids(video_ids),
                "document_count": len(documents),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print("FAISS index saved!")
    return vectorstore


def load_vectorstore(embeddings):
    vectorstore = FAISS.load_local(
        str(INDEX_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )
    print("FAISS index loaded!")
    return vectorstore