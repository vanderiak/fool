from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/involve')
def involve():
    return render_template('involve.html')

@app.route('/donation')
def donation():
    return render_template('donation.html')

if __name__ == '__main__':
    app.run(debug=True)