from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulação de um banco de dados
# Em um projeto real, você usaria um banco de dados de verdade (SQLAlchemy, por exemplo)
usuarios_db = {
    'admin@salao.com': {'senha': 'admin_password', 'role': 'admin'},
    'func1@salao.com': {'senha': 'func_password', 'role': 'employee'},
    'cliente1@email.com': {'senha': 'cliente_password', 'role': 'client'}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro_page():
    return render_template('cadastro.html') # Você precisará criar este arquivo

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')

    if email in usuarios_db and usuarios_db[email]['senha'] == senha:
        role = usuarios_db[email]['role']
        return jsonify({'success': True, 'role': role})
    else:
        return jsonify({'success': False, 'message': 'E-mail ou senha incorretos.'})

if __name__ == '__main__':
    app.run(debug=True)
