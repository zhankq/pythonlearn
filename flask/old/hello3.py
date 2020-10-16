from flask import Flask,escape,url_for,request,render_template,make_response,abort, redirect
app = Flask(__name__)

'''
# noinspection PyInterpreter
@app.route('/')
# def hello_world():
#     return 'Hello, World!'

def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
'''

#''' URL 构建'''
'''
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next="/"))
    print(url_for('profile', username='John Doe'))
'''

#HTTP 方法
'''
def do_the_login():
    return 'do_the_login'


def show_the_login_form():
    return "show_the_login_form"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
 '''
'''
#渲染模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return "Index Page"
'''


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('uploaded_file.txt')

    return render_template('upload.html')

@app.route('/setcookie')
def set_cookie():
    resp = make_response(render_template('upload.html'))
    resp.set_cookie('username', 'the username value')
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    return username+"--"

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

def this_is_never_executed():
    return 'this_is_never_executed'

'''
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404
'''
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    resp.headers['X-Job'] = 'Jobs'
    return resp
