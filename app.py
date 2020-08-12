from Poker.controller import app, socket


if __name__ == '__main__':
    socket.run(app, debug=True)
