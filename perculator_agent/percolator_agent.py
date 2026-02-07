import os
from tree_sitter import Language, Parser
import openai

RUST_LANG_PATH = "build/my_rust.so"

if not os.path.exists(RUST_LANG_PATH):
    Language.build_library(
        RUST_LANG_PATH,
        ["tree-sitter-rust"]
    )

RUST = Language(RUST_LANG_PATH, "rust")
parser = Parser()
parser.set_language(RUST)

openai.api_key = os.environ.get("OPENAI_API_KEY")

def parse_file(path):
    code = open(path, "rb").read()
    tree = parser.parse(code)
    return tree, code

def extract_items(tree, code):
    cursor = tree.walk()
    items = []
    stack = [cursor.node]

    while stack:
        node = stack.pop()
        if node.type in ("function_item", "struct_item", "enum_item"):
            snippet = code[node.start_byte:node.end_byte].decode("utf8","ignore")
            items.append((node.type, snippet))
        stack.extend(node.children)

    return items

def summarize(kind, snippet):
    prompt = f"""Explain this Rust {kind}:

{snippet}
"""

    resp = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.1
    )
    return resp.choices[0].message["content"]

def generate_docs(root=".", out="DOCS_AUTO.md"):
    with open(out,"w") as f:
        f.write("# Auto Generated Docs\n\n")
        for r,_,files in os.walk(root):
            for file in files:
                if file.endswith(".rs"):
                    path = os.path.join(r,file)
                    tree,code = parse_file(path)
                    items = extract_items(tree,code)
                    if not items:
                        continue
                    f.write(f"## {path}\n\n")
                    for k,s in items:
                        f.write(f"### {k}\n")
                        f.write(summarize(k,s))
                        f.write("\n\n")

if __name__ == "__main__":
    generate_docs()
