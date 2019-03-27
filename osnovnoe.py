from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


Message = namedtuple('Message', 'text tag')
messages = []

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html',messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text=request.form['text']
    tag=request.form['tag']
    messages.append(Message(text, tag))
    return redirect(url_for('main'))

@app.route('/registr', methods=['GET'])
def registration():
    return render_template('registration.html')

@app.route('/signin', methods=['GET'])
def signin():
    return render_template('Signin.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)