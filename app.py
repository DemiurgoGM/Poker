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
    deck = Deck()
    for _ in range(0, 7):
        random.shuffle(deck.cards_list)
    if request.args.get('phase') is None:
        user = request.args
        player = Player(user['user'], user['value'])
        return render_template('PlayPoker.html',
                               username=player.user, value=player.money, deck=deck)
    else:
        user = request.args  # expected args: user/value/phase/text/
        pass


if __name__ == '__main__':
    app.run()
