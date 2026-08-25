from flask import Flask, render_template, request, redirect, jsonify

application = Flask(__name__)

# In-memory notes list (resets if the app restarts — that's fine for learning)
notes = []

@application.route("/")
def home():
    return render_template("index.html", notes=notes)

@application.route("/add", methods=["POST"])
def add_note():
    text = request.form.get("note")
    if text:
        notes.append(text)
    return redirect("/")

@application.route("/health")
def health():
    return jsonify({"status": "ok", "note_count": len(notes)})

if __name__ == "__main__":
    application.run(debug=True)