import  stories
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """ Homepage
    contains a form for prompting user for all the words in the story
    """

    prompts = stories.story.prompts
    return render_template('story_form.html', prompts = prompts)


@app.route('/story')
def story():
    """ Homepage
    contains a form for prompting user for all the words in the story
    """
    story_text = stories.story.generate(request.args)
    return render_template('story.html', story_text = story_text)