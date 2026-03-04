# 📰 Real-Time News Summarisation Web Application

A Flask-based web application that extracts real-time news articles and generates concise summaries using Natural Language Processing (NLP).

This project demonstrates an end-to-end pipeline including data extraction, web scraping, text preprocessing, NLP-based summarisation, and web deployment.

---

## 🚀 Demo

https://github.com/SaurabhSRP/NewsApp_Flask/assets/108528607/f62b21b3-83e5-4118-ab70-4f85015a63a1

---

## 📌 Project Overview

We often rely on news applications that provide short and readable summaries of lengthy articles.  
This project replicates that concept by building a web application that:

- Fetches real-time news articles  
- Extracts article content  
- Cleans and processes raw text  
- Generates 60–100 word summaries  
- Displays results in a user-friendly interface  

The application currently limits output to the top 5 articles per category to optimise performance and readability.

---

## 🛠 Tech Stack

**Backend**
- Python 3.8
- Flask

**Data Processing & NLP**
- Newspaper3k
- BeautifulSoup4
- urllib

**Frontend**
- HTML
- CSS

**Data Source**
- Google News API

---

## ⚙️ System Architecture

1. Fetch real-time news using Google News API  
2. Extract full article content using web scraping  
3. Clean and preprocess text data  
4. Apply NLP-based summarisation  
5. Render summarised results in Flask web interface  

---

## 🧠 NLP Approach

The original design aimed to implement a BERT-based transformer summarisation model for improved contextual understanding.

Due to local hardware constraints, the deployed version uses Newspaper3k’s built-in summarisation engine.

A separate Python file containing a BERT-based implementation is included for future scalability and enhancement.

---

## 📊 Key Features

✔ Real-time news extraction  
✔ Automated data cleaning and preprocessing  
✔ NLP-based text summarisation  
✔ Category-based filtering (Politics, Sports, Finance, Entertainment)  
✔ Optimised response time (Top 5 articles per category)  
✔ Modular and extensible code structure  

---

## 🔮 Future Enhancements

- Deploy transformer-based summarisation using HuggingFace / BERT  
- Cloud deployment (Azure / Render)  
- Add sentiment analysis for news articles  
- Improve summarisation quality with adjustable word limits  
- Implement database storage for historical news tracking  

---

## 📂 How to Run Locally

Clone the repository:

```bash
git clone https://github.com/SaurabhSRP/NewsApp_Flask.git
cd NewsApp_Flask
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 📎 Repository Link

https://github.com/SaurabhSRP/NewsApp_Flask

---

## 📈 What This Project Demonstrates

- End-to-end data pipeline development  
- Real-time API integration  
- Web scraping and text preprocessing  
- Applied NLP for text summarisation  
- Backend development using Flask  
- Ability to design scalable data applications  

---

### 👤 Author
Saurabh Parave  
Master of Data Science – RMIT University  
