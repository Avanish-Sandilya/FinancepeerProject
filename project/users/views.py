# users/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from project import db
from project.models import User
from project.users.forms import RegistrationForm,LoginForm,UpdateUserForm

users = Blueprint('users',__name__)

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)



# login
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')
            next = request.args.get('next')
            if next ==None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html',form=form)

# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))
    elif request.method == "GET":
        form.username.data = current_user.username
    return render_template('account.html', form=form)

@users.route('/<username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username = username).first_or_404()
    complaint_posts = ComplaintPost.query.order_by(ComplaintPost.date.desc()).paginate(page, per_page=10)
    print(complaint_posts)
    return render_template('user_complaint_posts.html', complaint_posts=complaint_posts, user=user)











# user's list of Blog posts
