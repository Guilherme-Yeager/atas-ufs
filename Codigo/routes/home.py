from flask import Blueprint, render_template, redirect, url_for, session


home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/')
@home_bp.route('/index')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login.login'))
    return render_template('index.html')
