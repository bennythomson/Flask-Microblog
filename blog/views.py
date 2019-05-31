from blog import app, render_template, request, database, models, db, flash, redirect, g
from blog.models import Post, User
from blog import session

@app.route('/')
def index():
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
    else:
        user = None
    return render_template('index.html',  posts=Post.query.all(), user=user)

@app.route('/post', methods=['GET'])
def post_render():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():

    newPost = Post(name=request.form['name'], body=request.form['body'])
    db.session.add(newPost)
    db.session.commit()
    return render_template('index.html', posts=Post.query.all())

@app.route('/post/<post_id>')
def single(post_id):
    singlePost = Post.query.filter_by(id=post_id).first()
    return render_template('single.html', post=singlePost)

@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error_builder = None
        if not username:
            error_builder += "Username is required \n"
        if not password:
            error_builder += "Password is required \n"

        if error_builder is None:
            user = User.query.filter_by(username=username).first()

            if user is None or not user.check_password(password):
                flash("Doesnt exist or password is wrong")
            else:
                session['user_id'] = user.id
                redirect('/')
        else:
            flash(error_builder)

    return render_template('login.html')
