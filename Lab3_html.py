from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('text.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('dynamicURL.html', name = username)



if __name__ == '__main__':
    app.run()