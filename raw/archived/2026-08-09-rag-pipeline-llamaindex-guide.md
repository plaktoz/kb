# Building a RAG Pipeline with LlamaIndex: A Step-by-Step Guide

Source: https://pallab29.medium.com/building-a-rag-pipeline-with-llamaindex-a-step-by-step-guide-1c7964e6d06a

*By Pallab Sarangi · Oct 10, 2025*

---

## Overview

RAG (Retrieval-Augmented Generation) enhances LLMs by pulling relevant information from custom data before generating responses — useful for document-based chatbots and knowledge bases.

This guide uses **LlamaIndex** with a Hugging Face embedding model and Google's Gemini LLM.

---

## Prerequisites

```bash
pip install llama-index torch transformers google-generativeai
```

A Google API key from [Google AI Studio](https://aistudio.google.com) is also required.

---

## Step 1: Environment Setup

Configure embedding and language models via `Settings`:

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5-gguf")
Settings.llm = GoogleGenAI(model_name="models/gemini-pro", api_key="YOUR_GOOGLE_API_KEY")
```

---

## Step 2: Loading and Processing Documents

Load a PDF and split it into chunks using `SentenceSplitter`:

```python
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

documents = SimpleDirectoryReader(input_files=['RL economic paper.pdf']).load_data()
text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
Settings.text_splitter = text_splitter
```

---

## Step 3: Creating and Storing the Vector Index

Generate embeddings and persist the index to disk:

```python
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(documents, transformations=[text_splitter])
index.storage_context.persist(persist_dir="./storage")
```

---

## Step 4: Loading Index & Configuring the Query Engine

Reload from disk and set up a custom prompt template:

```python
from llama_index.core import load_index_from_storage, StorageContext
from llama_index.core.prompts import PromptTemplate
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

template = """
You are a helpful assistant... Use the following pieces of context to answer the question.
\nQuestion: {query}\nContext: {context}\nAnswer:"""

prompt_template = PromptTemplate(
    template=template,
    template_var_mappings={"query_str": "query", "context_str": "context"}
)

retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
response_synthesizer = get_response_synthesizer()
query_engine = RetrieverQueryEngine(retriever=retriever, response_synthesizer=response_synthesizer)
query_engine.update_prompts({"response_synthesizer:text_qa_template": prompt_template})
```

---

## Step 5: Querying

```python
response = query_engine.query("What are the main findings of the paper?")
print(response)
```

---

## Conclusion

Key areas for further exploration include:
- Different embedding/LLM models
- Alternative chunking strategies
- Advanced retrieval techniques (e.g., reranking)
- Building a UI layer

**GitHub:** [https://github.com/above-avg/rag-llama](https://github.com/above-avg/rag-llama)
