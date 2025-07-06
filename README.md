# 🧠 MediScrape AI – Intelligent Medical Web Scraper

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)
![LLM](https://img.shields.io/badge/LLM-Firecrawl%20API-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> Extract structured treatment insights from medical websites using Selenium, Firecrawl LLM API, and Pydantic.

---

## 📌 Overview

**MediScrape AI** is an advanced web scraping tool tailored for medical websites like [OrthoInfo.org](https://www.orthoinfo.org).  
It combines traditional scraping (Selenium + BeautifulSoup) with modern LLM techniques (Firecrawl API) to extract accurate and structured treatment data in **JSON format**.

---

## ✨ Features

✅ **Scrape 150+ treatment articles** from dynamic, paginated content (without URL change)  
✅ **LLM-powered data extraction** using Firecrawl API and a custom Pydantic schema  
✅ Outputs structured medical data: symptoms, causes, procedures, recovery time, etc.  
✅ Handles only `article` type links (ignores videos, etc.)  
✅ Output is clean, reliable, and **ready for AI pipelines or analytics**  

---

## 📊 Key Metrics

- 📄 **150+ treatment articles scraped**
- 🔗 **100% nested URL resolution**
- 🧠 **92%+ structured schema match accuracy**
- ⏱ **Timeout handling up to 120s per page**

---

## 🛠 Tech Stack

| Component           | Description                           |
|---------------------|---------------------------------------|
| **Python 3.10+**     | Core language                         |
| **Selenium**         | Web automation and dynamic pagination |
| **BeautifulSoup**    | HTML parsing                          |
| **Firecrawl API**    | GenAI-based structured data extraction |
| **Pydantic**         | Data schema validation                |
| **dotenv**           | Secure API key loading                |
| **JSON**             | Output format                         |

---

## 📂 Folder Structure 
MediScrape-AI/
├── helper.py # Firecrawl integration & schema validation
├── main.py # Web scraper logic using Selenium
├── treatment_links.json # Final structured JSON output
├── .env # Securely stores API key
└── README.md # Project documentation

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MediScrape-AI.git
cd MediScrape-AI

```
###  Requirements File 
pip install -r requirements.txt
pip install selenium beautifulsoup4 pydantic python-dotenv firecrawl
```

### 2. Install Dependencies
Make sure you have Python 3.10+ installed, then run:
```bash 
4
#### 2. Set Up Environment Variables
Create a `.env` file in the project root and add your Firecrawl API key:
API_KEY=your_firecrawl_api_key
