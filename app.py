from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from text_summarizer import nltk_summarizer
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/learn')
def learn():
    return render_template('learn.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        bigtext = request.form['bigtext']

        final_summary = nltk_summarizer(bigtext)
    return render_template('result.html', bigtext=bigtext, final_summary=final_summary)


if __name__ == '__main__':
    app.run(debug=True)
