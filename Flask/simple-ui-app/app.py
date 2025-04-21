from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog")
def contact():
    return render_template("blog.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


if __name__ == "__main__":
    app.run(debug = True, port = 8000)