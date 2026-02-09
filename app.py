from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        username="John",
        date=datetime.now().strftime("%Y-%m-%d"),
        items=['Apple', 'Banana', 'Orange']
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
