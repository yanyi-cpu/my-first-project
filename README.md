# 🤖 AI Chat Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
> 一个基于 DeepSeek 大模型与 Streamlit 框架构建的智能聊天助手。
> 本项目实现了流畅的多轮对话、会话历史管理以及云端部署，旨在探索大语言模型在 Web 应用中的最佳实践。

---

## 🚀 在线体验 (Live Demo)

项目已成功部署至 Streamlit Cloud，点击以下按钮即可立即体验：

👉 **[点击此处访问在线应用](https://my-ai-chatbot1999.streamlit.app/)**

---

## 📖 项目简介

**AI Chat Assistant** 是一个轻量级但功能完整的 AI 对话应用。它通过集成 DeepSeek 强大的大语言模型 API，为用户提供了一个自然、智能的交互界面。

该项目不仅是一个聊天工具，更是我对 **Python 全栈开发**、**API 集成**以及**云端 DevOps 流程**的一次完整实践。从本地编码调试到最终公网部署，每一步都体现了严谨的工程化思维。

---

## 🛠️ 技术栈

*   **前端交互**：`Streamlit` - 快速构建美观的 Web 界面，支持流式响应输出。
*   **AI 核心**：`DeepSeek API` - 接入 `deepseek-v4-pro` 模型，提供高质量的对话能力。
*   **数据持久化**：Python `json` 模块 - 实现会话记录的本地存储与读取。
*   **版本控制**：`Git` & `GitHub` - 规范的代码管理与版本迭代。
*   **云端部署**：`Streamlit Cloud` - 自动化 CI/CD 流程，实现应用的公网访问。

---

## ✨ 核心功能

### 1. 沉浸式流式对话
*   利用 `st.chat_message` 和 `stream=True` 实现了类似 ChatGPT 的**打字机效果**，极大提升了用户的阅读体验。
*   支持多轮对话上下文记忆，模型能够理解连续的对话逻辑。

### 2. 会话历史管理
*   自动保存聊天记录到本地 JSON 文件，刷新页面不丢失。
*   提供侧边栏管理功能，用户可以查看历史对话或开启新话题。

### 3. 参数自定义
*   用户可在侧边栏动态调整模型的 `Temperature`（创造力）和 `Max Tokens`（回复长度），定制个性化体验。

---

## 📂 本地运行指南

如果你想将项目克隆到本地运行，请确保已安装 Python 3.7+，然后依次执行以下命令：

```bash
# 1. 克隆项目仓库
git clone https://github.com/你的用户名/你的仓库名.git
cd 你的仓库名

# 2. 安装项目所需的依赖库
pip install -r requirements.txt

# 3. 配置 DeepSeek API Key
# 请创建 .streamlit/secrets.toml 文件并填入你的 Key
# 内容格式如下：
# DEEPSEEK_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"

# 4. 启动 Streamlit 应用
streamlit run ai界面.py
