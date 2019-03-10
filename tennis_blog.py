from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        'author': 'Rafa Nadal',
        'title': 'One More Injury',
        'content': 'Retired from Indian Wells and Miami tournaments. Sadness :(',
        'date_posted': 'March 1, 2019'
    },
    {
        'author': 'Maria Sharapova',
        'title': 'My First Disqualification',
        'content': 'Never again meldonium',
        'date_posted': 'March 3, 2019'
    }]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home_page.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about_page.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
