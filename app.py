from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Kunci rahasia untuk sesi

@app.route('/')
def home():
    if 'name' in session:
        return render_template('index.html', name=session['name'])
    return render_template('name.html')

@app.route('/set_name', methods=['POST'])
def set_name():
    session['name'] = request.form['name']
    return render_template('index.html', name=session['name'])

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    name = session.get('name', 'User')
    if 'kabar' in user_message.lower():
        response = f"Saya baik, bagaimana dengan Anda, {name}? Apakah kabar Anda baik atau tidak?"
        options = ["Baik", "Tidak Baik"]
    elif 'hari ini' in user_message.lower():
        response = f"Hari ini sangat menyenangkan! Bagaimana dengan hari Anda, {name}?"
        options = []
    elif 'umur' in user_message.lower():
        response = f"Pembuat saya belum memberikan saya umur, tapi menurut saya anda lebih tua dari saya, {name}! Bagaimana dengan umur Anda?"
        options = []
    elif 'aul' in user_message.lower():
        response = f"Pembuat saya pernah mabar dengan kakak itu dan dia sangat menyenangkan! Bagaimana dengan Anda, {name}, apakah mengenal aul juga?"
        options = []
    elif 'hero' in user_message.lower():
        response = f"Menurut saya kamu harus menggunakan hero harith, {name}, apakah kamu bisa menggunakan harith?"
        options = []
    else:
        response = f"Hallo, {name}, ini chat bot dibuat oleh Mahveen. Ada yang bisa saya bantu?"
        options = []

    return render_template('index.html', user_message=user_message, response=response, options=options, name=name)

@app.route('/response', methods=['POST'])
def response():
    user_choice = request.form['choice']
    name = session.get('name', 'User')
    if user_choice == "Baik":
        response = f"Senang mendengar kabar Anda baik, {name}! 😊"
    else:
        response = f"Jangan khawatir, {name}, semuanya akan baik-baik saja. Tetap semangat! 💪"

    return render_template('index.html', user_message=user_choice, response=response, options=[], name=name)

if __name__ == '__main__':
    app.run(debug=True)
