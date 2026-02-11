# Legal RAG Assistant with Endee Vector Database

## 🎯 Project Overview

**Legal RAG Assistant** is a complete AI-powered legal document analysis system built as part of an AI/ML project assignment. This project demonstrates practical implementation of modern AI technologies with a focus on vector database integration and Retrieval-Augmented Generation (RAG) workflows.

### **Key Features:**
- **Endee Vector Database Integration** - Efficient semantic search and storage
- **RAG Pipeline Implementation** - Context-aware document retrieval and generation
- **Semantic Search** - Natural language querying of legal documents
- **Web Application Interface** - Modern, responsive 5-page web interface
- **Mock Mode Operation** - No external API dependencies required
- **Comprehensive Testing Suite** - Validation of all functionality
- **Production-Ready Code** - Clean architecture with error handling

## 🏗️ Architecture Overview
<img src="screenshots/architecture.png" alt="Home" height ="300" width="450" style="border-radius: 8px; border: 1px solid #e5e7eb;">

## 🚀 Quick Start & Demo

### **📋 Prerequisites**
- Python 3.8 or higher
- Git (for cloning repository)
- Web browser (Chrome, Firefox, Edge)

### **⚡ Installation & Setup**
```bash
# 1. Clone the repository
git clone https://github.com/Sunny22110010324/legal-rag-endee.git
cd legal-rag-endee

# 2. Install dependencies
pip install -r requirements.txt
```

**🌐 Access the Application**
Once running, open your browser and navigate to:
```bash
👉 http://localhost:5000
```

**Check the Working of the Use Case**

**Step 1 – Upload a Legal Document**
1. Navigate to the Upload Page
2. Upload a legal document (PDF or TXT)
3. Wait for confirmation message:
```bash
Document processed successfully
```
**This Confirms:**
1. Document chunking works
2. Embeddings are generated
3. Data stored in Endee Vector DB

**Step 2 – Verify Document Storage**

1. Go to the Documents Page
2. Ensure the uploaded document appears in the list

**Confirms:**

Vector database storage is successful

**Step 3 – Test Semantic Search**

1. Navigate to the Search Page
2. Enter a query such as:
```bash
   Contract
```
3. Click Search

**Expected Behavior:**

1. Relevant document chunks are retrieved
2. Results are meaning-based (semantic similarity)
3. Not simple keyword matching

**Running the Test Suite**

To validate backend functionality:

```bash
python app.py
```
**Expected Output:**
```bash
All tests passed successfully
```

**📸 Screenshots & Demonstration**

## 📸 Screenshots & Demonstration

### **Application Interface Gallery**

<div align="center">

| | | |
|:---:|:---:|:---:|
| **🏠 Home Page** | **💬 Chat Interface** | **🔍 Search Interface** |
| <img src="screenshots/home.png" alt="Home" width="250" style="border-radius: 8px; border: 1px solid #e5e7eb;"> | <img src="screenshots/chat.png" alt="Chat" width="250" style="border-radius: 8px; border: 1px solid #e5e7eb;"> | <img src="screenshots/search.png" alt="Search" width="250" style="border-radius: 8px; border: 1px solid #e5e7eb;"> |
| *Dashboard & Navigation* | *AI Legal Assistant* | *Semantic Search* |
| **⬆️ Upload Interface** | **📁 Documents Management** | **📊 All Features** |
| <img src="screenshots/upload.png" alt="Upload" width="250" style="border-radius: 8px; border: 1px solid #e5e7eb;"> | <img src="screenshots/documents.png" alt="Documents" width="250" style="border-radius: 8px; border: 1px solid #e5e7eb;"> | <div style="padding: 20px; background: #f8fafc; border-radius: 8px; border: 1px dashed #cbd5e1;"><strong>5 Screenshots Total</strong><br>Each demonstrating a key feature of the Legal RAG Assistant</div> |
| *Document Processing* | *Database Management* | *Complete System* |

</div>

**🧠Tech Stack**

1. Python
2. Flask

3. Endee Vector Database

4. Retrieval-Augmented Generation (RAG)

5. HTML, CSS, JavaScript

6. Mock LLM Mode
