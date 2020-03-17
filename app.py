import random

from flask import Flask, render_template, request

from models.Deck import Deck
from models.Player import Player

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('default.html')


@app.route('/PlayPoker.html')
def play_poker():
    user = request.args
    player = Player(user['user'], user['value'])
    deck = Deck()
    random.shuffle(deck.cards_list)
    return render_template('PlayPoker.html',
                           username=player.user, value=player.money, deck=deck)


if __name__ == '__main__':
    app.run()
