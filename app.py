from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'chave_secreta_super_simples'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        role = request.form.get('role')

        session['usuario'] = usuario
        session['role'] = role
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.errorhandler(404)
def erro_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erro_500(e):
    return jsonify({
        "sucesso": False,
        "dados": None,
        "erro": "Ocorreu um erro interno no servidor."
    }), 500

if __name__ == '__main__':
    app.run(debug=True)