from ast import literal_eval
from random import shuffle

from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user

from Poker.controller import app, db, bcrypt
from Poker.models.Deck import Deck, compare_hands
from Poker.models.Player import Player, Hand
from Poker.models.dbModel import User


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if current_user.is_active:
        logout_user()
    if request.form:
        user = request.form
        hash_password = bcrypt.generate_password_hash(user.get('password')).decode('utf-8')
        if User.query.filter_by(username=user.get('user')).first():
            return render_template('default.html', message='Username already taken. Please choose another one.')
        elif User.query.filter_by(email=user.get('EmailSignin')).first():
            return render_template('default.html', message='E-mail already taken. Please choose another one.')
        new_user = User(
            username=user.get('user'), email=user.get('EmailSignin'), password=hash_password, savings=user.get('money'))
        db.session.add(new_user)
        db.session.commit()
        return render_template('default.html', success=True)
    elif request.args:
        return render_template('default.html', message=request.args.get('message'))
    return render_template('default.html')


@app.route('/PlayPoker', methods=['GET', 'POST'])
def play_poker():
    if request.form:
        form = request.form
        if current_user.is_active:
            return Play_Poker_Form_work(form)
        else:
            user = User.query.filter_by(username=form.get('user')).first()
            if user and bcrypt.check_password_hash(user.password, form.get('password')):
                login_user(user, remember=False)
                return Play_Poker_Form_work(form)
            else:
                return redirect(url_for('homepage', message='Something went wrong, check your login and try again.'))
    else:
        return redirect(url_for('homepage', message='Something went wrong, please try again.'))


def Play_Poker_Form_work(form):
    deck = Deck()
    for _ in range(5):
        shuffle(deck.cards_list)

    if form.get('info'):
        info = literal_eval(form.get('info'))
        info['round'] = int(info['round']) + 1
        info['blind'] = int(info['blind']) if int(info['round']) % 10 != 0 else int(info['blind']) + 100
        return render_template('PlayPoker.html', info=info, deck=deck,
                               Hand=Hand, make_player=Player, compare_hands=compare_hands)
    else:
        information = {
            "user": form.get('user'),
            "money": form.get('money'),
            "round": int(form.get('round')) + 1,
            "blind": int(form.get('blind')) if int(form.get('round')) % 10 != 0 else int(form.get('blind')) + 100
        }
        return render_template('PlayPoker.html', info=information, deck=deck,
                               Hand=Hand, make_player=Player, compare_hands=compare_hands)


@app.route('/logOut')
def logouttoHomePage():
    logout_user()
    return redirect(url_for('homepage'))
