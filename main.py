from flask import Flask, render_template, request, url_for, redirect
from flask_misaka import Misaka
import os

app = Flask(__name__)
Misaka(app)

def get_mds():
    section = 'helloworld'
    cheatsheets = []
    for file in os.listdir('./cheatsheets'):
        cheatsheets.append(str(file).replace('.md',''))
    return sorted(cheatsheets)

@app.route('/')
def hello():
    return render_template('index.html', mds=get_mds())

@app.route('/about')
def about():
    return render_template('about.html', mds=get_mds())

@app.route('/cheat')
def cheat():
    global section
    with open(f'./cheatsheets/{section}.md', 'r') as f:
        data = f.read()
    return render_template('cheatsheet.html', data=data, mds=get_mds())

@app.route('/b')
def b():
    global section
    section = request.args.get('section', None)
    return redirect(url_for('cheat'))

if __name__ == '__main__':
    app.run(debug=True, port=5687, host='0.0.0.0')