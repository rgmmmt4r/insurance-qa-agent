import os, glob, sys
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MODEL = "claude-sonnet-4-6"

def load_docs(folder="docs"):
    if not os.path.isdir(folder):
        print(f"錯誤：找不到資料夾 '{folder}/'，請建立並放入 .md 文件。", file=sys.stderr)
        sys.exit(1)
    paths = sorted(glob.glob(f"{folder}/*.md"))
    if not paths:
        print(f"錯誤：'{folder}/' 中沒有任何 .md 文件。", file=sys.stderr)
        sys.exit(1)
    docs = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            docs.append(f"### 來源檔案：{os.path.basename(path)}\n{f.read()}")
    return "\n\n".join(docs)

def ask(question, knowledge):
    instructions = (
        "你是保險資訊問答助理。只能根據下方提供的文件回答，"
        "不可自行編造。若文件中找不到答案，明確說「文件中查無相關資訊」。"
        "回答時請註明依據哪一份來源檔案。"
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=800,
        system=[
            {"type": "text", "text": instructions},
            {
                "type": "text",
                "text": f"=== 可用文件 ===\n{knowledge}",
                "cache_control": {"type": "ephemeral"},
            },
        ],
        messages=[{"role": "user", "content": question}],
    )
    u = resp.usage
    print(
        f"[cache: write={u.cache_creation_input_tokens} "
        f"read={u.cache_read_input_tokens} "
        f"input={u.input_tokens} output={u.output_tokens}]"
    )
    return resp.content[0].text

if __name__ == "__main__":
    knowledge = load_docs()
    print("保險問答 Agent（輸入 q 離開)")
    while True:
        q = input("\n你的問題：")
        if q.strip().lower() == "q":
            break
        print("\n" + ask(q, knowledge))
