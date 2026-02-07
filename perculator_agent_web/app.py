
import os
import openai
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from agent import CodeIndexer

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = FastAPI()
indexer = CodeIndexer()

if os.path.exists("index.faiss"):
    indexer.load()

@app.get("/", response_class=HTMLResponse)
async def home():
    return open("index.html").read()

@app.post("/ask")
async def ask(req: Request):
    data = await req.json()
    q = data["question"]
    ctx = "\n".join(indexer.query(q))

    prompt = f"""Answer using this code context:

{ctx}

Question: {q}
"""

    resp = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.1
    )

    return {"answer": resp.choices[0].message["content"]}

@app.post("/index")
async def build():
    indexer.ingest(".")
    indexer.save()
    return {"status":"indexed"}
