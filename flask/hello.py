from flask import  Flask,escape
app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "hello,World"
@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello ,World"

@app.route("/user/<username>")
def show_user_profile(username):
    ## show the user profile for that user
    return "User %s" % escape(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route("/projects/")
def projects():
    return "The project pate"

@app.route("/about")
def about():
    return "The about page"
