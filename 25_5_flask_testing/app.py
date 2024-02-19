from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

#good 
@app.route('/')
def display_boggle_board():
    game_board = boggle_game.make_board()
    session['game_board'] = game_board
    
    return render_template('index.html', game_board = game_board)


#good
@app.route('/check_word')
def check_word():
    word = request.args['word'] # word in request.args['word'] is from the query arguments from URL like /check_word?word=hello
    board = session['game_board']
    response = boggle_game.check_valid_word(board, word)
    # print("Return of the checkvalid word function: ", response)
    
    return jsonify({'result': response})
