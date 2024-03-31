# def main():
#     print(f"File Name is :{__name__}")


# if __name__ == "__main__":
#     main()


#####################
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align:center; color:red'>Hello World</h1>"


@app.route("/about")
def about():
    return "About Page"


@app.route("/page/<int:number>")  # Specify the 'number' parameter as an integer
def page(number):  # Add 'number' parameter to the function
    return f"This is Page {number}"


@app.route("/page/<name>")  # Specify the 'number' parameter as an integer
def name(name):  # Add 'number' parameter to the function
    return f"Welcome {name}"


if __name__ == "__main__":
    app.run(debug=True)
