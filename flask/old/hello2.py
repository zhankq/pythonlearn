from flask import Flask,escape,url_for,request
app = Flask(__name__)


url_for('static', filename='style.css')

@app.route("/")
def index():
    return "index"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<username>")
def profile(username):
    return "{}'s profile".format(escape(username))


@app.route("/logins",methods=["GET","POST"])
def logins():
    if request.method == "POST":
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'

# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("login"))
#     print(url_for("login",next="/"))
#     print(url_for("profile",username='John Doe'))
