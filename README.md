#  ThreatHuntAI: Intelligent Log Anomaly Detection

**ThreatHuntAI** is an intelligent anomaly detection system designed for analyzing large-scale system or security logs using **machine learning and NLP techniques**.  
It detects irregular log patterns using **TF-IDF vectorization**, **BERT/SentenceTransformer embeddings**, and **Isolation Forest models**, offering both statistical and semantic insights into anomalies.

---

##  Features

- **Data Cleaning & Preprocessing**
  - Removes IPs, timestamps, digits, and special symbols.
  - Normalizes text for vectorization and embedding.

- **Dual-Model Detection**
  - *TF-IDF + Isolation Forest* for lightweight anomaly detection.  
  - *BERT/SentenceTransformer embeddings + Isolation Forest* for semantic anomaly detection.

- **Visualization**
  - PCA-based cluster visualization (Normal vs Anomaly)
  - Log category distribution (rule-based classification)
  - Time-series anomaly trends over days

- **Anomaly Categorization**
  - Labels anomalies as: *Authentication Failure, Application Error, Network Event, Privilege Escalation*, etc.

- **Interactive UI**
  - Streamlit-based dashboard to:
    - Upload log files
    - View anomaly distribution
    - Explore sample anomalies
    - Download detected anomaly reports

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.10+ |
| Libraries | pandas, numpy, scikit-learn, transformers, sentence-transformers, seaborn, matplotlib |
| ML Models | IsolationForest, PCA |
| Embeddings | TF-IDF, BERT (or MiniLM) |
| UI | Streamlit + Plotly |

---

##  Project Structure
├── HDFS_2k.log                                                                  
Sample dataset (logs)                                                                                   
├── threathunt_main.ipynb                                                                                        
Main Jupyter Notebook                                                                                         
├── threathunt_ui.py                                                                                        
Streamlit web interface                                                                                     
├── Detected_Anomalies_combined.csv                                                                         
Output anomaly report                                                                                             
├── requirements.txt                                                                                                                      
 Dependencies                                                                                                       
└── README.md                                                                                                
 This file



## Setup Instructions
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ThreatHuntAI.git
cd ThreatHuntAI

# Install dependencies
pip install -r requirements.txt


