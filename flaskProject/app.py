from flask import Flask
app = Flask(__name__)

result = {'success': True}

@app.route('/')
def hello_world():  # put application's code here
    return result

if __name__ == '__main__':
    app.run()

