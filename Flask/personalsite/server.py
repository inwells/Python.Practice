from flask import Flask, render_template
from random import randint
app = Flask(__name__)

number = randint(1,10)
print(number)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()