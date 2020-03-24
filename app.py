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
    if request.args.get('phase') is None:
        deck = Deck()
        for _ in range(0, 7):
            random.shuffle(deck.cards_list)
        user = request.args
        player = Player(user['user'], user['value'])
        return render_template('PlayPoker.html',
                               username=player.user, value=player.money, deck=deck,
                               blind=2, phase='start', text='', round=1)
    elif request.args.get('phase') == 'start':
        user = request.args  # expected args: user/value/phase/text/deck/blind/round
        player = Player(user['user'], user['value'])
        deck = Deck()
        for _ in range(0, 7):
            random.shuffle(deck.cards_list)
        blind = user['blind'] if int(user['round']) % 10 != 0 else int(user['blind']) + 2
        return render_template('PlayPoker.html', username=player.user, value=player.money, deck=deck,
                               blind=blind, round=int(user['round'])+1,
                               phase='start', text='')
    else:
        pass


if __name__ == '__main__':
    app.run()
