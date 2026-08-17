# AskDesk

[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)](https://www.postgresql.org/)

**AskDesk** is a multi-tenant FAQ and support chatbot platform. It allows users to create their own intelligent customer support bots grounded entirely in their own custom knowledge base, powered by **Retrieval-Augmented Generation (RAG)**.

This repository serves as the core engine for AskDesk, demonstrating production-grade RAG architecture, vector search, and LLM integrations.

---

## Architecture Overview

AskDesk operates on a standard production RAG pipeline:

1. **Ingestion Flow:** 
   Raw Text → Text Chunking → Embedding Model → PostgreSQL (`pgvector`)
2. **Query Flow:** 
   User Question → Hybrid Search → Re-ranking → Context Merging → LLM API → Grounded Answer

---

## Features

* **Multi-Tenant Architecture:** Securely host multiple bots across different owners, with strict data isolation.
* **Knowledge Base Ingestion:** Easily paste FAQs, documentation, or support materials. Text is automatically chunked, embedded, and stored for high-speed vector retrieval.
* **Retrieval-Augmented Generation (RAG):** Answers are grounded strictly in the provided knowledge base using hybrid search (vector + keyword) to prevent LLM hallucinations.
* **Custom Instructions:** Bot owners can define custom system prompts to control their bot's personality, tone, and specific boundaries.
* **Session-Based Chat:** Frictionless experience for end-users. No accounts required; chat history is seamlessly maintained via browser sessions.

---

## Tech Stack

* **Backend Framework:** [Django](https://www.djangoproject.com/) (Python)
* **Database & Vector Store:** [PostgreSQL](https://www.postgresql.org/) with [`pgvector`](https://github.com/pgvector/pgvector)
* **Embeddings:** Self-hosted `sentence-transformers` or Gemini Embedding APIs
* **LLM Generation:** Google Gemini API

---

## Local Development Setup

### Prerequisites
* Python 3.10+
* PostgreSQL 15+ (with the `pgvector` extension installed)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/askdesk.git
   cd askdesk
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r dev-requirements.txt
   ```

4. **Environment Variables:**
   Copy the example environment variables file and fill in your details:
   ```bash
   cp .env.example .env
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

---

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/askdesk/issues).
