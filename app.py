from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form4', methods=['GET', 'POST'])
def form4():
    if request.method == 'POST':
        tanlov = request.form.get('tanlov')
        return f"<h2>Siz tanlagan: {tanlov}</h2><br><a href='/'>Orqaga</a>"
    return render_template('form4.html')

if __name__ == '__main__':
    app.run(debug=True)
