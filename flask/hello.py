from flask import Flask,escape,request,render_template
app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "Hello World!2d"
@app.route('/')
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello, World"
@app.route("/user/<username>")
def show_user_profile(username):
    #show the user profile for that user
    return "User {username}".format(username=username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    #    # show the post with the given id, the id is an integer
    return "Post {:d}".format(post_id)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath {}".format(escape(subpath))

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about")
def about():
    return "The about page"

@app.route("/login",methods=["POST","GET"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"],request.form["password"]):
            return "good jobs ,username: " + request.form["username"] +" password: "+ request.form["password"]
        else:
            error = 'Invalid username/password'

    searchword = request.args.get('key', '')
    print(searchword)

    return render_template('login.html', error=error,searchword=searchword)



#################文件上传¶


def valid_login(name,pwd):
    '''
    :param name:
    :param pwd:
    :return:
    '''
    if name=="vancekq" and pwd=="123456":
        return True
    return False

