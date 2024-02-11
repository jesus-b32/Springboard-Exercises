from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = [] # As people answer questions, you should store their answers in this list.
number_of_questions = 0
question_number = 0
current_survey = ''


@app.route('/')
def choose_survey():
    """ choose survey page
    render a page that shows the user survey options to complete. 
    The button should serve as a link that directs the user to the first question
    """

    return render_template('pick_survey.html', surveys = surveys)


@app.route('/select_survey/post', methods=['POST'])
def survey_post():
    """ post handle
    Handle form data from survey selected  by user. 
    """
    global current_survey
    current_survey = surveys[request.form['surveys']]

    global number_of_questions
    number_of_questions = len(current_survey.questions)

    return redirect('/start_survey')


@app.route('/start_survey')
def survey_start_page():
    """ start page
    render a page that shows the user the title of the survey, the instructions, and a button to start the survey. 
    The button should serve as a link that directs the user to the first question
    """
    title = current_survey.title
    instructions = current_survey.instructions

    global question_number
    question_number = 0

    global responses
    responses.clear()

    return render_template('start_page.html', title = title, instructions = instructions)


@app.route('/questions/<int:question_id>')
def question_pages(question_id):
    """ questions
    Display form where user can answer questions to the survey
    """
    if (len(responses) != question_id):
        flash('Invalid question ID entered. Please complete the survey in order.')
        return redirect(f'/questions/{question_number}')

    question = current_survey.questions[question_id].question
    choices = current_survey.questions[question_id].choices

    return render_template('question.html', 
                           question = question, 
                           choices = choices, 
                           question_id = question_id)


@app.route(f'/questions/post', methods=['POST'])
def questions_post():
    """ post handle
    Handle form data from questioned answered by user. 
    When user answered all questions, redirect them to thank you page.
    Otherwise, redirect to next question.
    """
    responses.append(request.form['choices'])
    global question_number
    question_number += 1

    if question_number == number_of_questions: # answered all questions
        return redirect('/thank_you')

    return redirect(f'/questions/{question_number}')


@app.route('/thank_you')
def complete_page():
    """ 
    Survey complete. Show completion page.
    """
    return render_template('thank_you.html')