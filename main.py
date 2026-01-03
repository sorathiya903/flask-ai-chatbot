from flask import Flask, render_template, request, jsonify 
from google import genai
import os
import webbrowser as wb
app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
print(api_key)
@app.route("/") 
def home():
    return render_template("index.html") 
@app.route("/chat", methods=["POST"]) 
def chat(): 
    user_input = request.json.get("message") 
    if "open youtube" in user_input:
     wb.open_new("youtube.com")
    return
    if "open google" in user_input:
     wb.open_new("google.com")
    
    try: 
        response = client.models.generate_content( model="models/gemini-2.5-flash", contents=user_input ) 
        return jsonify({"reply": response.text}) 
    
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__": 
    app.run()




