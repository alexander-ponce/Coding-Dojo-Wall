from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, post



@app.route('/create/post', methods=['POST'])
def create_post():
    user= session['user_id']
    if not post.Posts.validate_post(request.form):
        return redirect (f"/user/account/{user}")
    print(session['user_id'])
    print(request.form)
    post.Posts.save_post(request.form)
    # id_data={
    #     'id': id
    # }
    
    # one_user= user.Users.get_one(id_data)

    return redirect (f'/user/account/{user}')

@app.route('/posts/delete/<int:id>')
def delete_post(id):
    if 'user_id' not in session:
        return redirect('/')
    id_data={
        'id': id
    }
    post.Posts.delete_post(id_data)
    user= session['user_id']
    return redirect(f'/user/account/{user}')


