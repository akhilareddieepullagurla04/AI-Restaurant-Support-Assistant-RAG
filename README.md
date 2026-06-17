# AI-Restaurant-Support-Assistant-RAG

## Overview

AI Restaurant Support Assistant is a Retrieval-Augmented Generation (RAG) application that answers customer support questions related to restaurant and food delivery services.

The system retrieves information from policy documents and FAQs stored in a vector database and uses a Large Language Model (Groq Llama 3) to generate accurate responses.

---

## Features

* Restaurant support chatbot
* Semantic search using ChromaDB
* Retrieval-Augmented Generation (RAG)
* Groq Llama 3 integration
* Source document retrieval
* Streamlit user interface

---

## Tech Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq Llama 3
* Streamlit

---

## Project Structure

```text
AI-Restaurant-Support-Assistant-RAG/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   └── llm.py
│
├── data/
│   ├── refund_policy.txt
│   ├── delivery_policy.txt
│   ├── cancellation_policy.txt
│   ├── coupon_policy.txt
│   └── faq.txt
│
└── chroma_db/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-Restaurant-Support-Assistant-RAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Build Vector Database

```bash
python rag/ingest.py
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Questions

* How do refunds work?
* Can I cancel my order after preparation starts?
* My order is delayed by 25 minutes.
* Can I combine two coupons?

---

## Future Improvements

* PDF document support
* Hybrid search
* Reranking
* Ticket classification
* Human escalation workflow
* Multi-language support

---

## Author
Akhila Pullagurla

Built as a GenAI / RAG portfolio project.
