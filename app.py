from flask import Flask, render_template
app = Flask(__name__)

@app.route('/fizzbuzz')
def hello():
    return render_template("fizz.html")

if __name__ == '__main__':
    app.run()