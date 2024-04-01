from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/option", methods=["GET", "POST"])
def option():
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("xss_input")  # Corrected 'from' to 'form'
    return render_template(
        "option.html", user_input=user_input
    )  # Passing user_input to the template


# MongoDB connection settings
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "pyhack"


# Function to establish MongoDB connection
def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db


@app.route("/login", methods=["GET", "POST"])
def login():
    user_input = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Connect to MongoDB
        db = get_db()

        # Example: Inserting username and password into a collection named 'users'
        users_collection = db.users
        user_data = {"username": username, "password": password}
        users_collection.insert_one(user_data)

        user_input = f"Username: {username}, Password: {password}"

    return render_template("login.html", user_input=user_input)


if __name__ == "__main__":
    app.run(debug=True)
