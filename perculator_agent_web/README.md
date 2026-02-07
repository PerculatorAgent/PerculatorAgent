
# PerculatorAgent Web

Adds embeddings + Q&A + web UI over your Percolator codebase.

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key
uvicorn app:app --reload
```

Open:

http://localhost:8000

Click **Index Repo**, then ask questions.

## What it does

- Builds embeddings over all .rs files
- Stores them in FAISS
- Retrieves relevant chunks
- Uses OpenAI for answers
- Simple browser UI

Educational prototype.
