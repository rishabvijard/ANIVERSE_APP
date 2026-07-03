# 🔥 ANIVERSE — Flask Web App

An animated anime streaming landing page, served with Python + Flask.

## 📁 Structure
```
ANIVERSE_APP/
├── app.py                 # Flask server
├── requirements.txt       # dependencies (Flask)
├── templates/
│   └── index.html         # the website (Jinja2 template)
└── static/
    ├── hero.mp4           # hero background video
    ├── hero.jpg           # hero poster image
    └── img/               # anime images (char1-9, ep1-4, spotlight)
```

## 🚀 Run it

1. (Optional) create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the server:
   ```
   python app.py
   ```
4. Open your browser at **http://127.0.0.1:5000**

## 🔌 Routes
| Route             | Description                       |
|-------------------|-----------------------------------|
| `/`               | Main ANIVERSE landing page        |
| `/api/characters` | JSON list of characters (example) |

## 🛠️ Customize
- Replace `static/hero.mp4` to change the background video.
- Swap any image in `static/img/` (keep the same filename).
- Edit `templates/index.html` for content/layout.
