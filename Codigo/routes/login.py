from flask import Blueprint, render_template, redirect, url_for, session


login_bp = Blueprint('login', __name__, url_prefix='/')

@login_bp.route('/login')
def login():
    if 'user_id' in session:
        return redirect(url_for('home.index'))
    return render_template('login.html')
