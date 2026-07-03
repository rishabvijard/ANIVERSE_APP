"""
ANIVERSE — Flask web app
Serves the animated anime website.

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the main ANIVERSE landing page."""
    return render_template("index.html")


# Optional JSON endpoint — handy if you later want to load data dynamically.
@app.route("/api/characters")
def characters():
    from flask import jsonify
    return jsonify([
        {"name": "Blade of Flame",     "anime": "Demon Slayer",        "tier": "S+", "power": 99},
        {"name": "Cursed Spirit King", "anime": "Jujutsu Kaisen",      "tier": "S",  "power": 94},
        {"name": "Water Breather",     "anime": "Demon Slayer",        "tier": "A+", "power": 91},
        {"name": "Shadow Hokage",      "anime": "Naruto",              "tier": "S",  "power": 93},
        {"name": "Gear Five",          "anime": "One Piece",           "tier": "S+", "power": 96},
        {"name": "Founding Power",     "anime": "Attack on Titan",     "tier": "S+", "power": 97},
        {"name": "Chainsaw Heart",     "anime": "Chainsaw Man",        "tier": "S",  "power": 95},
        {"name": "One For All",        "anime": "My Hero Academia",    "tier": "A+", "power": 90},
        {"name": "Fullmetal",          "anime": "Fullmetal Alchemist", "tier": "S+", "power": 96},
    ])


if __name__ == "__main__":
    # debug=True auto-reloads when you edit files
    app.run(host="127.0.0.1", port=5000, debug=True)
