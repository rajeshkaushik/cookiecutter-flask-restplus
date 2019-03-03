import os


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    from wsgi import app

    app.run(debug=True)
