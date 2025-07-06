# GOD-TIER MCP AUTO-PURCHASE STACK

This project is a full-stack solution for automated purchasing, featuring a stealth browser, multi-agent orchestration, and real-time notifications.

## Features

- **Stealth Browsing:** Utilizes GoLogin and Playwright for undetectable automation.
- **Multi-Agent System:** Leverages LangGraph and MetaGPT for complex task execution.
- **Vector Memory:** Uses Qdrant and MongoDB for logging and memory.
- **Web UI:** A Next.js frontend for triggering and monitoring tasks.
- **Real-time Notifications:** Telegram bot for instant updates.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd omni_purchase_stack
    ```

2. **Set up environment variables:**
    - Copy `.env.template` to `.env`
    - Fill in your credentials for GoLogin, OpenAI/Gemini, and Telegram.

3. **Run the stack:**

    ```bash
    docker-compose up --build -d
    ```

## Usage

- Access the web UI at `http://localhost:3000` to trigger a purchase.
- Interact with the Telegram bot for status updates.
