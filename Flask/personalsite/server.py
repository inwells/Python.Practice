from flask import Flask, render_template
from random import randint
import datetime as dt
app = Flask(__name__)

number = randint(1,10)
print(number)

@app.route('/')
def home():
    current_year = dt.datetime.today().year
    return render_template("index.html", year=current_year)

if __name__ == "__main__":
    app.run()