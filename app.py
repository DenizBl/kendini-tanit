from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tanitim', methods=['POST'])
def tanitim():
    ad = request.form.get('ad')
    yas = request.form.get('yas')
    sehir = request.form.get('sehir')
    hobiler = request.form.get('hobiler')
    return render_template('result.html', ad=ad, yas=yas, sehir=sehir, hobiler=hobiler)

if __name__ == '__main__':
    app.run(debug=True)
