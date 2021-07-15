#-----------------------------------------------------------------------
# Agregador de Links
#-----------------------------------------------------------------------

import time
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

#-----------------------------------------------------------------------

accounts = {
    'vonkakarius': '959595'
}

trees = {
    'vonkakarius': {
        'Instagram': 'instagram.com/vonkakarius',
        'Facebook': 'facebook.com/vonkakarius',
        'Twitter': 'twitter.com/vonkakarius',
        'Telegram': 'telegram.org/vonkakarius'
    }
}

#-----------------------------------------------------------------------

@app.route('/')
def home():
    return 'Página inicial, carecendo de html'

#-----------------------------------------------------------------------

@app.route('/signup')
def signup():
    return render_template('signup.html')

#-----------------------------------------------------------------------

@app.route('/signup/save', methods=['POST', 'GET'])
def save_account():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user')
        password = request.args.get('password')

    global accounts
    accounts[user] = password
    return redirect(url_for('edit', user=user))

#-----------------------------------------------------------------------

@app.route('/login')
def login():
    return render_template('login.html')

#-----------------------------------------------------------------------

@app.route('/login/verification', methods=['POST', 'GET'])
def verif_login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user')
        password = request.args.get('password')

    if user in accounts and accounts.get(user) == password:
        return redirect(url_for('edit', user=user))
    else:
        return 'Quem erra o login é gay'

#-----------------------------------------------------------------------

@app.route('/edit/<user>')
def edit(user):
    return f'Página de edição da linktree de {user}'

#-----------------------------------------------------------------------

@app.route('/<user>')
def tree(user):
    if user in trees:
        return render_template('tree.html', links=trees[user])
    else:
        return f'Quando houver links cadastrados pra {user}, essa página exibirá.'

#-----------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

#-----------------------------------------------------------------------