from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def display_boggle_board():
    """Renders the boggle board game html template

    Returns:
        html template: Boggle board game
    """
    
    game_board = boggle_game.make_board()
    session['game_board'] = game_board
    highest_score = session.get('highest_score', 0) #defaults to 0 if there is no highscore value
    number_of_games = session.get('number_of_games', 0) #defaults to 0 if there is no num of games value
    
    return render_template('index.html', game_board = game_board,
                           highest_score = highest_score,
                           number_of_games = number_of_games)



@app.route('/check_word')
def check_word():
    """Check if user entered word is valid

    Returns:
        JSON: Response of the check_valid_word function
    """
    
    word = request.args['word'] # word in request.args['word'] is from the query arguments from URL like /check_word?word=hello
    board = session['game_board']
    response = boggle_game.check_valid_word(board, word)
    
    return jsonify({'result': response})

@app.route('/game_over', methods = ['POST'])
def game_over():
    """Store score of user if it is a new high score. Increment number of games played. Stored both in sessions.

    Returns:
        JSON: True or false on whether new record was set
    """
    
    highest_score = session.get('highest_score', 0)
    number_of_games = session.get('number_of_games', 0)
    score = request.json['score']
    
    new_record = score > highest_score
    if(new_record):
        session['highest_score'] = score
        
    session['number_of_games'] = number_of_games + 1
    
    return jsonify({'new_record' : new_record})