
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

class CodeIndexer:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks = []

    def ingest(self, root):
        texts = []
        for r,_,files in os.walk(root):
            for f in files:
                if f.endswith(".rs"):
                    path = os.path.join(r,f)
                    txt = open(path,"r",errors="ignore").read()
                    for i in range(0,len(txt),1500):
                        chunk = txt[i:i+1500]
                        self.chunks.append(chunk)
                        texts.append(chunk)

        embeddings = self.model.encode(texts)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def save(self):
        faiss.write_index(self.index,"index.faiss")
        pickle.dump(self.chunks,open("chunks.pkl","wb"))

    def load(self):
        self.index = faiss.read_index("index.faiss")
        self.chunks = pickle.load(open("chunks.pkl","rb"))

    def query(self,q,k=4):
        emb = self.model.encode([q])
        D,I = self.index.search(emb,k)
        return [self.chunks[i] for i in I[0]]
