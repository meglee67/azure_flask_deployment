# this is example code taken from Hant's repo here: https://github.com/hantswilliams/HHA_504_2023/blob/main/WK2/flaskapp_0/app.py and then modified for the assignment

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

# replace the OG Hants link for a CSV file to your own unique file.
df = pd.read_csv('data/2015.csv')
@app.route('/data')
def data(data=df):
    data = data.head(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )