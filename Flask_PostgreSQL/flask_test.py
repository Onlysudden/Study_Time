from flask import Flask
from flask import render_template
from flask import request
# from flask import make_response


app = Flask(__name__)


@app.route('/json')
def json():
    return dict(request.args.lists())


@app.route('/args/')
def args():
    return render_template(
        'args.html',
        title='Arguments',
        query=request.args.lists()
    )


@app.route('/99-bottles')
def bottles():
    return render_template('bottles.html')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)


# Проверка json - http://127.0.0.1:5000/json?a=1&a=2&b=3
