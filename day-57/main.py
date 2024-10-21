from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get("https://api.npoint.io/7e3c5df9b18824667b16").json()
    return render_template("index.html", data=data)


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    data = requests.get("https://api.npoint.io/7e3c5df9b18824667b16").json()
    return render_template("post.html", data=data, id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
