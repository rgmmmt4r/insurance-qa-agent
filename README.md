# Insurance QA Agent / 保險問答 Agent

A minimal CLI agent that answers insurance-related questions strictly based on the Markdown documents under `docs/`. Powered by the Claude API with prompt caching.

一個極簡的命令列問答 Agent，僅依據 `docs/` 內的 Markdown 文件回答保險相關問題。使用 Claude API，並啟用 prompt caching。

## Setup / 安裝

```bash
# Activate the virtual environment / 啟用虛擬環境
source venv/bin/activate

# Install dependencies / 安裝相依套件
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API key:

請在專案根目錄建立 `.env`，並填入 API 金鑰：

```
ANTHROPIC_API_KEY=your_key_here
```

## Usage / 使用方式

```bash
python agent.py
```

Type a question at the prompt. Enter `q` to quit.

在提示處輸入問題；輸入 `q` 離開。

## Project Structure / 專案結構

```
.
├── agent.py          # CLI entry point / 主程式
├── docs/             # Knowledge base (Markdown) / 知識庫文件
├── requirements.txt  # Python dependencies / Python 套件
└── .env              # API key, gitignored / API 金鑰（不入版控）
```
