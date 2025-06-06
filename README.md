# 📝 Flask To-Do App with Git Branching & MongoDB Integration

🚀 Project Overview
This project is a Flask-based To-Do app that demonstrates advanced Git branching workflows, JSON API routing, and MongoDB integration. Built as a college assignment to practice collaborative Git techniques.

📂 Project Structure
flask-todo-app/
│
├── app.py                # Flask application
├── data.json             # JSON file used by /api route
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Basic frontend styling
├── templates/
│   └── index.html        # Frontend form (To-Do items)

📌 Features
- REST API route `/api` serving data from `data.json`
- Frontend form for To-Do item submission
- POST route `/submittodoitem` to MongoDB Atlas
- Git branching strategy for collaboration and version control:
  - main, kesarwanikhushi, kesarwanikhushi_new, master_1, master_2
- Git rebase, reset, merge conflict resolution

🛠️ How to Run Locally
1. Clone the Repository:
   git clone git@github.com:yourusername/flask-todo-app.git
   cd flask-todo-app

2. Install Dependencies:
   pip install -r requirements.txt

3. Run the Flask App:
   python app.py

4. Visit in Browser:
   http://localhost:5000/

🌐 MongoDB Configuration
Make sure to configure your MongoDB URI in app.py:
client = pymongo.MongoClient("your_mongodb_connection_string")

📸 Screenshots
> Add your screenshots here once you complete the assignment steps (setup, form, API test, MongoDB proof, etc.)

✅ Branch Summary
- kesarwanikhushi – Initial Flask setup and commit
- kesarwanikhushi_new – JSON update and merge conflict practice
- master_1 – Frontend To-Do form development
- master_2 – Backend API to handle To-Do submissions
- main – Final integrated version

📄 License
This project is licensed for educational use only.
