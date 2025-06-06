from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connect to MongoDB (update your connection string accordingly)
client = MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.ghfnzgu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['todo']
collection = db['items']

# Load API data from JSON
@app.route('/api', methods=['GET'])
def api_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# Route to render frontend form
@app.route('/')
def index():
    return render_template('index.html')

# Route to accept form submission
@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    name = request.form['itemName']
    desc = request.form['itemDescription']
    print("Item Name:", name)
    print("Description:", desc)
    return "Item submitted!"
collection.insert_one(submit_item)
print("Item submitted!")
