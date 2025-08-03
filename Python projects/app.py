from flask import Flask, render_template
import random

app = Flask(__name__)

jokes = [
    "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
    "Why was the JavaScript developer sad? Because they didn’t 'null' their feelings."
]

@app.route('/')
def index():
    joke = random.choice(jokes)
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
