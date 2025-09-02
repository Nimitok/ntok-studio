from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.ntok_demo


sample_data = [
{"prompt": "Hello AI", "result": "AI response for: Hello AI"},
{"prompt": "Tell me about hackathons", "result": "AI response for: Tell me about hackathons"},
]


db.generations.insert_many(sample_data)
print("Seed data inserted!")