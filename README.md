# 🛡️ Phishing URL Detection using Machine Learning

A machine learning-based web application that detects phishing websites using URL analysis. The system helps users identify suspicious links before visiting potentially harmful websites.

## 👥 Team Members

- **Saniya Santosh Choughule**
- **Iqra Mohd Nisar Khan**

## 🧠 Project Goal

To develop a machine learning-based tool that detects phishing websites using only the URL — helping users avoid falling victim to fraudulent sites before they click.

## 🔍 Problem Statement

Phishing is a deceptive technique used by attackers to trick individuals into revealing sensitive data by impersonating trusted websites. These fake sites are commonly distributed via URLs designed to look legitimate. Manual detection is difficult, and traditional blacklist-based approaches often fail to catch newly created phishing links.

This project uses **Machine Learning** to analyze URL characteristics and classify a URL as **Phishing** or **Legitimate** in real time.

## 💡 Features

- ✅ User-friendly web interface built with Streamlit
- ✅ Real-time phishing URL detection
- ✅ Random Forest Classifier for reliable, accurate predictions
- ✅ Trained on a real-world dataset of labeled URLs
- ✅ Instant URL analysis with clear results
- ✅ Dark-themed, responsive UI
- ✅ Simple and easy to use — no technical knowledge required

## ⚙️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Web Interface | Streamlit |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Model Persistence | Joblib |

## 📊 Machine Learning Model

**Algorithm:** Random Forest Classifier
**Dataset:** Phishing URL Dataset (Kaggle) — containing labeled legitimate and phishing URLs

**Workflow:**
1. Data Collection
2. Feature Extraction
3. Model Training
4. Model Evaluation
5. URL Prediction via Web Interface

### Feature Extraction

The system extracts key URL characteristics such as:
- URL length
- Presence of HTTPS
- Number of dots
- Special characters
- Domain information
- Suspicious URL patterns

### Prediction Flow

Extracted features → passed to the trained Random Forest model → model classifies the URL as **Legitimate** or **Phishing** → result displayed instantly on the web interface.

## 🛠️ Project Structure

```
Phishing_URL_Detection/
│
├── tool/
│   └── source_code/
│       ├── train_model.py       # Trains the ML model using URL dataset
│       ├── predict_cli.py       # CLI for predicting phishing/legit URLs
│       ├── phishing_model.pkl   # Saved trained ML model
│       └── dataset.csv          # Dataset used for training/testing
│
├── phishing-env/                # Python virtual environment (not uploaded)
│
├── Research_Paper.pdf           # Final research paper for internship
├── Presentation.pdf             # Slide deck explaining project
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Files/folders to ignore in Git
```

## 🔄 How It Works — Visual Flow

```
+----------------+     +------------------+     +------------------+
|  User Input    |     | Feature          |     | Random Forest    |
|  (URL to Check)|---->| Extraction       |---->| Model             |
+----------------+     +------------------+     | (phishing_model.pkl)
        ^                       |                +------------------+
        |                       v                        |
+----------------+     +------------------+               |
|  Display       |<----| URL Prediction   |<--------------+
|  Result        |     | (Predict URL)    |
+----------------+     +------------------+
```

## 🖥️ Web Application Interface

1. User enters a URL into the input field
   ```
   https://google.com/
   ```
2. Clicks **"Check URL"**
3. System analyzes the URL and displays the result:
   ```
   ✅ Legitimate URL
   ```
   or
   ```
   ⚠️ Phishing URL
   ```

## 🚀 How to Run the Project

**1. Clone the Repository**
```bash
git clone https://github.com/Iqrakhan0670/Phishing-Detection-using-URL-Analysis.git
cd Phishing-Detection-using-URL-Analysis
```

**2. Set Up Environment**
```bash
python -m venv phishing-env
phishing-env\Scripts\activate   # On Windows
pip install -r requirements.txt
```

**3. Train the Model (Optional)**
```bash
python train_model.py
```

**4. Run the Streamlit Application**
```bash
python -m streamlit run app.py
```

**5. Open in Browser**
```
http://localhost:8501
```

## 📷 Screenshots

**Web Application — Legitimate URL Detected**
![Web App Screenshot]("C:\Users\IQRA KHAN\OneDrive\Gambar\Screenshots\Screenshot 2026-08-02 140946.png")

**CLI Version — Prediction Output**
![CLI Screenshot](screenshots/cli_output.png)

*(Add your screenshot images to a `screenshots/` folder in the repo and update the paths above to match your filenames.)*

## 🎯 Applications

- Cybersecurity Awareness
- Safe Web Browsing
- Educational Demonstration
- Phishing Prevention
- Security Research

## 🎥 Demo Video

👉 [Watch on YouTube](https://youtu.be/xAaTMeI30cI?si=WIquzm39vT4EUyrY)

## 📄 License

This project is licensed under the **MIT License** and developed for educational and research purposes only.

## ⚠️ Disclaimer

This project is a demonstration of ML-based phishing detection. Predictions may not always be 100% accurate and should not be considered a substitute for professional, enterprise-grade cybersecurity solutions.

## 📚 References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- Phishing URL Dataset (Kaggle)
- Python Official Documentation
