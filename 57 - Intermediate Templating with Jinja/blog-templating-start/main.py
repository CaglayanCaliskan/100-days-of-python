from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(url).json()
post_object = []

for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_object.append(post_obj)


@app.route('/')
def blog():
    return render_template("index.html", data=post_object)


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for blog_post in post_object:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", data=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
