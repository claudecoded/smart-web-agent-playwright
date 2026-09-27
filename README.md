# Smart Web Agent Playwright

An AI-powered web automation agent built with **Playwright**, **Browser-Use**, and **LangChain**. This repository provides a stealth, vision-capable AI agent configured to navigate complex websites (such as Amazon) by mimicking real human interactions and dynamically handling dynamic layouts.

---

## 🚀 Features

* **AI-Driven Navigation**: Uses GPT-4o to visually analyze pages and click/type without hardcoded CSS selectors.
* **Anti-Bot Evading Layout**: Pre-configured browser flags to bypass common automation detection mechanisms (`AutomationControlled`).
* **Visual Understanding**: Processes screenshots in real-time to solve multi-step navigation flows.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:
* **Python 3.10 or higher**
* **pip** (Python package installer)
* An active **OpenAI API Key** (with access to `gpt-4o`)

---

## 🛠️ Step-by-Step Installation

Follow these exact steps to set up the project locally on your machine.

### 1. Clone the Repository
Open your terminal (or PowerShell/Command Prompt) and run:
```bash
git clone https://github.com
cd smart-web-agent-playwright
```
*(Note: Replace `YOUR_USERNAME` with your actual GitHub username).*


### 2. Install Dependencies
Install all required Python libraries specified in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers
Download and configure the necessary Chromium binaries required for Playwright automation:
```bash
playwright install chromium
```

---

## ⚙️ Environment Configuration

For security reasons, API keys are managed via environment variables and are **never** pushed to GitHub.

1. In the root directory of the project, create a new file named `.env`.
2. Open the `.env` file in your favorite text editor and paste your OpenAI API key using the following format:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
```

> ⚠️ **Important:** Make sure there are no spaces or quotes around your key. The `.gitignore` file is already configured to keep this file private.

---

## 💻 How to Run the Agent

Once everything is installed and configured, launch the AI agent by executing the main script:

```bash
python agent.py
```

### What happens next?
* A **Chromium browser window will open** automatically.
* You will see the AI Agent interacting with the website in real-time (typing, scrolling, and clicking).
* The terminal will print a live history of the agent's thoughts and actions, followed by the final extracted data summary.

---

## 📄 License & Disclaimer

This repository is for educational, research, and data-analysis purposes only. Please ensure full compliance with the Terms of Service (ToS) and robots.txt guidelines of any website you interact with. The author is not responsible for any misuse of this tool.
