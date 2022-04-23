from flask import Flask
from random import randint
app = Flask(__name__)

number = randint(1,10)
print(number)

@app.route('/')
def home():
    return "<h1>guess a number between 1 and 10</h1><br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route('/<int:num>')
def return_response(num):
    if num == number:
        return "<h1 style='color:green;'>You found me!</h1><br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif num > number:
        return "<h1 style='color:blue;'>nope, too high</h1><br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif num < number:
        return "<h1 style='style:red;'>nope, too low</h1><br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

if __name__ == "__main__":
    app.run()