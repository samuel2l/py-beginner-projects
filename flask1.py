from flask import Flask, render_template,request
import random
import time
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about")
def abtt():
    return "<p>Aboput page bishhh</p>"


# eg to pass param to route
# this is allowed but must be enclosed in <>
# normally used when a certain func deps on user input, eg:
@app.route("/pth/<path:username>")
def accepting_variables(username):
    rand_num = random.randint(1, 20)

    return render_template("index.html", num=rand_num, year=time.ctime().split()[-1])


@app.route("/guess/<username>")
def guess_age(username):
    params = {
        "name": username,
        "country": "Ghana",

    }
    response = requests.get("https://api.agify.io", params=params)

    return render_template("index.html", name=username, age=response.json()["age"], count=response.json()["count"])


@app.route("/blog")
def blogs():
    response = requests.get(url="https://api.npoint.io/ac54e715e11fd4100d4e")
    data = response.json()
    print(data)

    return render_template("blog.html", posts=data)


@app.route("/blog/<int:index>")
def full_blog(index):
    # for blog_post in data:
    #     if blog_post.id == index:
    #         requested_post = blog_post

    response = requests.get(url="https://api.npoint.io/ac54e715e11fd4100d4e")
    data = response.json()[index]
    print(data)
    return render_template("full_blog.html", full_post=data)
@app.route("/contact")
def contact_form():
    return render_template("contact_form.html")

@app.route("/login", methods=["POST"])
def receive_data():
    #looks like variable name must be the same
    email=request.form["email"]
    message=request.form["message"]
    return f"<h1>Name: {email}, message: {message}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
