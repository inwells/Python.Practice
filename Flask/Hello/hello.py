from flask import Flask
import requests
app = Flask(__name__)

def make_h1(function):
    def wrapper_function():
        return f'<h1>{function()}</h1>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route('/')
@make_h1
@make_emphasis
@make_underlined
def hello_world():
    return 'hello world!'


@app.route('/guess/<name>')
def guess(name):
    gen_response = requests.get(f"https://api.genderize.io/?name={name}")
    gen_data = gen_response.json()
    age_response = requests.get(f"https://api.agify.io/?name={name}")
    age_data = age_response.json()
    return f'Hello {name.title()}!<p>I think that you are a {gen_data["gender"]}</p><p>You may be {age_data["age"]} years old.</p'

if __name__ == "__main__":
    app.run()