from flask import Flask, render_template, request, jsonify
from google import genai
import os
import webbrowser as wb

app = Flask(__name__)

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"error": "No message received"})

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash-lite",
            contents=user_input
        )
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()


