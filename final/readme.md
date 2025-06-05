# 🥬 Final Project: Vegetable Growing Assistant using ChromaDB & OpenAI

## 📌 Overview  
This project is a lightweight **Retrieval-Augmented Generation (RAG)** system that helps answer questions about growing vegetables in Florida. It combines document-based semantic search with OpenAI’s GPT model to provide grounded and accurate responses based only on local PDF data.

## 🔍 Category  
**AI + Data Application (RAG & NLP)**  
**Type:** Custom implementation using LangChain, ChromaDB, and OpenAI  
**AI Support:** Architecture, querying, and code structure guided by ChatGPT  

## 🎯 Objectives  
- Build a document-aware Q&A assistant using vector search  
- Use local PDFs as the only source of truth  
- Practice retrieval-augmented generation (RAG) concepts  
- Work with ChromaDB for persistent embedding storage  
- Generate responses using OpenAI GPT models, limited by data context  

## 🏗️ How It Works  
1. Load vegetable-growing PDFs using `PyPDFDirectoryLoader`  
2. Split into chunks using `RecursiveCharacterTextSplitter`  
3. Embed & store documents into ChromaDB (`PersistentClient`)  
4. When a question is asked:
   - Perform semantic search to retrieve top-matching chunks  
   - Feed the chunks into GPT as a prompt  
   - GPT answers strictly using that data  

## 📁 Project Structure  
├── data/ ← Place your vegetable PDFs here
├── chroma_db/ ← Vector database (auto-generated)
├── load_and_store.py ← Script to load, chunk & store PDFs
├── ask.py ← Script to ask questions from stored data
├── .env ← Your OpenAI API key
└── requirements.txt ← Python dependencies
