from flask import Flask,render_template,Markup,request,make_response,jsonify
app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    app.logger.debug('A value for debugging')
    return render_template("hello.html",name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
 #       return request.form['username']
        return jsonify({'status': '0', 'errmsg': '登录成功！'})


    return render_template("hello.html")

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value error'
    return resp

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
