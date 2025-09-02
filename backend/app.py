from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os


app = Flask(__name__)
CORS(app)


# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client.ntok_demo


# Fake AI generator (replace with OpenAI or other)
def generate_with_ai(prompt):
return f"AI response for: {prompt}"


@app.route("/api/generate", methods=["POST"])
def generate():
data = request.json
prompt = data.get("prompt", "")
result = generate_with_ai(prompt)
db.generations.insert_one({"prompt": prompt, "result": result})
return jsonify({"result": result})


@app.route("/api/history", methods=["GET"])
def history():
items = list(db.generations.find({}, {"_id": 0}))
return jsonify(items)


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=True)