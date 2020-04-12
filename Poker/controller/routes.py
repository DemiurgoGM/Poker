from random import shuffle

from flask import render_template, request

from Poker.controller import app
from Poker.models.Deck import Deck
from Poker.models.Player import Player


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def homepage():
    user = request.form
    if user:
        print(user)  # TODO
    return render_template('default.html')


@app.route('/PlayPoker', methods=['GET', 'POST'])
def play_poker():
    if request.args.get('phase') is None:
        deck = Deck()
        for _ in range(0, 7):
            shuffle(deck.cards_list)
        user = request.args
        player = Player(user['user'], user['money'])
        return render_template('PlayPoker.html',
                               username=player.user, money=player.money, deck=deck,
                               blind=100, phase='start', text='', round=1)
    elif request.args.get('phase') == 'start':
        user = request.args  # expected args: user/value/phase/text/deck/blind/round
        player = Player(user['user'], user['money'])
        deck = Deck()
        for _ in range(0, 7):
            shuffle(deck.cards_list)
        blind = int(user['blind']) if int(user['round']) % 10 != 0 else int(user['blind']) + 100
        return render_template('PlayPoker.html', username=player.user, money=player.money, deck=deck,
                               blind=blind, round=int(user['round']) + 1,
                               phase='start', text='')
    else:
        return "Else statement"  # TODO
