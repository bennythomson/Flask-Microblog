from blog import app, render_template, request, database, models, db
from blog.models import Post

@app.route('/')
def index():
    return render_template('index.html',  posts=Post.query.all())

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
