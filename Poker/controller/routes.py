
from ast import literal_eval
from random import shuffle

from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user
from flask_socketio import emit

from Poker.controller import app, db, bcrypt, socket
from Poker.models.CompareHandsFuncs import compare_hands
from Poker.models.Deck import Deck, Hand
from Poker.models.dbModel import User

# Deck is a global variable
deck = Deck()


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if current_user.is_active:
        logout_user()
    if request.form:
        # adding new user to database
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
        # if the player is already playing, continue
        if current_user.is_active:
            return Play_Poker_Form_work(form)
        else:
            # if he's entering the game now
            user = User.query.filter_by(username=form.get('user')).first()
            if user and bcrypt.check_password_hash(user.password, form.get('password')):
                login_user(user, remember=False)
                return Play_Poker_Form_work(form)
            else:
                return redirect(url_for('homepage', message='Something went wrong, check your login and try again.'))
    else:
        return redirect(url_for('homepage', message='Something went wrong, please try again.'))


def Play_Poker_Form_work(form):

    # getting computer money
    computer_money = int(form.get('computer_money')) if form.get('computer_money') else int(form.get('money'))

    # suffling the deck
    for _ in range(3):
        shuffle(deck.cards_list)

    # Setting the hands
    player_hand = Hand(deck.pop(), deck.pop())
    computer_hand = Hand(deck.pop(), deck.pop())
    table_hand = deck.get_n_cards(5)

    # Readding the cards to the deck
    deck.addCard(player_hand.this_hand()[0], player_hand.this_hand()[1],
                 computer_hand.this_hand()[0], computer_hand.this_hand()[1])

    # Adding the table's hand to the players
    for card in table_hand:
        player_hand.addCard(card)
        computer_hand.addCard(card)
        deck.addCard(card)   # Readding the cards to the deck

    # Algorithm to find the best hand of the players
    player_hand.setBestHand()
    computer_hand.setBestHand()

    # finding who won
    compared_hands = compare_hands(player_hand.this_hand(), computer_hand.this_hand())
    if compared_hands == player_hand.this_hand():
        # player wins
        winner = 1
    elif compared_hands == computer_hand.this_hand():
        # computer wins
        winner = 2
    else:
        # tie
        winner = 3

    # String variable of the table
    flop = ''
    for i in range(3):
        flop = flop + str(table_hand[i]) + '<br>'
    # turn = table_hand[3]
    # river = table_hand[4]
    if form.get('info'):
        info = literal_eval(form.get('info'))  # String to dictionary
        info['round'] = int(info['round']) + 1
        info['blind'] = int(info['blind']) if int(info['round']) % 10 != 0 else int(info['blind']) + 100
        return render_template('PlayPoker.html',
                               info=info, winner=winner,
                               player_hand=player_hand, computer_hand=computer_hand,
                               computer_money=computer_money, money=form.get('money'),
                               flop=flop, turn=table_hand[3], river=table_hand[4])
    else:
        information = {
            "user": form.get('user'),
            "round": int(form.get('round')) + 1,
            "blind": int(form.get('blind')) if int(form.get('round')) % 10 != 0 else int(form.get('blind')) + 100
        }
        return render_template('PlayPoker.html',
                               info=information, winner=winner,
                               money=form.get('money'), player_hand=player_hand,
                               computer_hand=computer_hand, computer_money=computer_money,
                               flop=flop, turn=table_hand[3], river=table_hand[4])


@app.route('/PvP', methods=['GET', 'POST'])
def PlayerVsPlayer():
    if request.form:
        print(request.form)
        return render_template('PvP.html')
    else:
        return redirect(url_for('homepage', message='Something went wrong, please try again.'))


@socket.on('connect')
def handle_Test():
    print('message received')
    emit('message', 'message')


@app.route('/logOut')
def logouttoHomePage():
    logout_user()
    return redirect(url_for('homepage'))

