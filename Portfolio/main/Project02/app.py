from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice')
def roll_dice():
    dice1_number = random.randint(1, 6)
    dice2_number = random.randint(1, 6)
    return render_template('index.html', dice1=dice1_number, dice2=dice2_number)

if __name__ == '__main__':
    app.run(debug=True)
    