from flask import Flask, render_template, request, jsonify 
from google import genai
app = Flask(__name__)
client = genai.Client(api_key="AIzaSyDPXCrN7w-1S8JXgfC2msLuC5twiRRYnsE") 
@app.route("/") 
def home():
    return render_template("index.html") 
@app.route("/chat", methods=["POST"]) 
def chat(): 
    user_input = request.json.get("message") 
    try: 
        response = client.models.generate_content( model="models/gemini-2.5-flash", contents=user_input ) 
        return jsonify({"reply": response.text}) 
    
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__": 
    app.run(debug=True)