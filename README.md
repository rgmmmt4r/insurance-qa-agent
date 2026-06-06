# Insurance QA Agent / 保險問答 Agent

A minimal CLI agent that answers insurance-related questions strictly based on the Markdown documents under `docs/`. Powered by the Claude API with prompt caching. The agent cites its sources and refuses to answer beyond the provided documents.

一個極簡的命令列問答 Agent，僅依據 `docs/` 內的 Markdown 文件回答保險相關問題。使用 Claude API 並啟用 prompt caching，回答時標註來源，且不會超出文件範圍作答。

> ⚠️ All data in `docs/` is fictional and for demonstration only. It does not relate to any real insurance product or company.
> `docs/` 內所有資料皆為虛構，僅供展示用途，與任何真實保險商品或公司無關。

## Setup / 安裝

```bash
python3 -m venv venv           # Create virtual environment / 建立虛擬環境
source venv/bin/activate        # Activate / 啟用（Windows: venv\Scripts\activate）
pip install -r requirements.txt # Install dependencies / 安裝相依套件
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
├── docs/             # Knowledge base (fictional Markdown) / 知識庫文件（虛構）
├── CLAUDE.md         # AI collaboration rules / AI 協作規範
├── requirements.txt  # Python dependencies / Python 套件
└── .env              # API key, gitignored / API 金鑰（不入版控）
```

## Security & Compliance Notes / 資安與合規考量

- **Fictional data only / 全為虛構資料**：所有知識庫文件皆為虛構，與任何公司無關。
- **No secrets in version control / 金鑰不入版控**：API 金鑰以環境變數（`.env`）管理，已由 `.gitignore` 排除。
- **Grounded answers only / 僅依文件作答**：Agent 僅根據 `docs/` 內容回答，查無資料時明確告知，避免幻覺。
- **Traceable / 可追溯**：回答標註來源檔案，便於查證，呼應金融場景對可解釋性的要求。

## Business Extension / 商業延伸

此結構可延伸應用於實際保險業務場景，例如：

- **核保輔助 / Underwriting support**：快速查詢核保規則與條款。
- **智能客服 / Customer service**：即時回答客戶常見保單問題。
- **保單問答 / Policy QA**：協助業務員與客戶查找條款細節。

差別僅在於將虛構文件替換為真實內部文件，並加上**權限控管**與**操作稽核**機制，以符合金融業的資安與合規要求。

## Notes / 備註

本專案之 AI 協作規範部分參考公開社群資源，並依專案需求調整；專案相關內容為本人撰寫。
