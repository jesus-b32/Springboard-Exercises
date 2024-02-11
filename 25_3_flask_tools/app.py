from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route('/')
def choose_survey():
    """ choose survey page
    render a page that shows the user survey options to complete. 
    The button should serve as a link that directs the user to the first question
    """

    return render_template('pick_survey.html', surveys = surveys)


@app.route('/store_survey', methods=['POST'])
def store_survey():
    """ post handle
    Handle form data from survey selected  by user. 
    """
    #store survey choice in session
    survey_choice = request.form['surveys']
    session['current_survey'] = survey_choice

    return redirect('/start_survey')


@app.route('/start_survey')
def survey_start_page():
    """ start page
    render a page that shows the user the title of the survey, the instructions, and a button to start the survey. 
    The button should serve as a link that directs the user to the first question
    """
    current_survey = surveys[session['current_survey']]
    title = current_survey.title
    instructions = current_survey.instructions

    return render_template('start_page.html', title = title, instructions = instructions)


@app.route('/start_survey/post', methods=['POST'])
def session_post():
    """ 
    Create as session list to store user responses
    """
    session['responses'] = []

    return redirect('/questions/0')


@app.route('/questions/<int:question_id>')
def question_pages(question_id):
    """ questions
    Display form where user can answer questions to the survey
    """
    
    responses = session.get('responses')
    survey_choice = session.get('current_survey')
    current_survey = surveys[survey_choice]
    
    if(survey_choice is None):
        return redirect('/')
    
    if(responses is None):
        return redirect('/start_survey')
    
    # answered all questions
    if len(responses) == len(current_survey.questions):
        return redirect('/complete')
    
    # Trying to access questions out of order
    if (len(responses) != question_id):
        flash('Invalid question ID entered. Please complete the survey in order.')
        return redirect(f'/questions/{len(responses)}')

    # current_survey = session['current_survey']
    question = current_survey.questions[question_id].question
    choices = current_survey.questions[question_id].choices

    return render_template('question.html', 
                           question = question, 
                           choices = choices, 
                           question_id = question_id)


@app.route(f'/answer', methods=['POST'])
def answer():
    """  answer handle
    Handle form data from questioned answered by user. 
    When user answered all questions, redirect them to thank you page.
    Otherwise, redirect to next question.
    """
    # add the response to the session
    responses = session['responses']
    responses.append(request.form['choices'])
    session['responses'] = responses

    current_survey = surveys[session['current_survey']]
    if len(responses) == len(current_survey.questions):
        # answered all questions
        return redirect('/complete')

    return redirect(f'/questions/{len(responses)}')


@app.route('/complete')
def complete_page():
    """ 
    Survey complete. Show completion page.
    """
    return render_template('complete.html')