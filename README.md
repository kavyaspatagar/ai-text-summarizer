# 🧠 AI Text Summarizer App

This project is a simple web app that takes long paragraphs or articles and returns a concise summary using a pre-trained Transformer model from Hugging Face 🤖. Built with **Flask (Python)** for the backend and **HTML/CSS** for the frontend.

---

## 🚀 Features
```
- ✅ Summarize long text into a short summary
- ✅ Built using Hugging Face Transformers (e.g., BART)
- ✅ Python Flask backend
- ✅ Simple and clean HTML/CSS interface
```
---

## 🖥️ Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Frontend  | HTML, CSS                         |
| Backend   | Python, Flask                     |
| AI Model  | Hugging Face Transformers (BART) |


## ⚙️ Setup Instructions

### 💻 Prerequisites
```
- Python 3.7 or higher
- `pip` installed
- Internet connection (to download the pre-trained model)
```
### 🪟 Windows Setup

```bash
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### 🍎 macOS Setup

```bash
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

### 🐧 Linux Setup

```bash
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

### 🌐 How to Use
```
Run the app by executing python app.py (Windows) or python3 app.py (macOS/Linux)

Open a web browser and visit http://127.0.0.1:5000

Paste or type in the text you want to summarize

Click the Summarize button

View the summary displayed below the input box
````

### 📁 Project Structure

```text
ai-text-summarizer/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── static/
│   └── style.css        # CSS styles
├── templates/
│   └── index.html       # HTML template
└── .gitignore           # Files/folders to ignore in Git
```

### 📌 Notes

```
This app uses the sshleifer/distilbart-cnn-12-6 model from Hugging Face.

Model files are downloaded on first run and require internet connection.

For production usage, consider deploying on cloud platforms like Render, Hugging Face Spaces, or Heroku.

Windows users may need to run the command prompt as Administrator to create virtual environments.
```

### 📤 Deployment (Optional)

```
You can deploy this app on:

Render

Hugging Face Spaces

Heroku (requires additional setup)
```

Feel free to open issues or pull requests if you want to improve this project!
