"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return """
    <!doctype html>
    <html>
        <head>
            <title>Home Page</title>
            <link rel="stylesheet" href="static/madlibs.css">
        </head>

        <body>
        <h1>Hi! This is the home page.</h1>
        <p><a href="/hello">Say Hello</a></p>
        </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    wants_to_play = request.args.get("game")

    if wants_to_play == 'yes':
        return render_template("game.html")

    elif wants_to_play == 'no':
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    
    color = request.args.get("color")
    person = request.args.get("person")
    month = request.args.get("month")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    adjective2 = request.args.get("adjective2")
    adverb = request.args.get("adverb")
    verb = request.args.get("verb")
    noun2 = request.args.get("noun2")
    ing_verb = request.args.get("ing_verb")
    verb2 = request.args.get("verb2")

    return render_template("madlib_2.html", color = color, person = person, month=month, noun = noun, 
    adjective = adjective, adjective2=adjective2, adverb=adverb,
    verb = verb, noun2=noun2, ing_verb = ing_verb, verb2 = verb2)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
