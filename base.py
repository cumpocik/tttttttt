from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/clothing/')
def clothing():
    return render_template('clothing.html', products = products['clothing'])

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html', products=products['shoes'])

@app.route('/jacket/')
def jacket():
    return render_template('jacket.html', products=products['jacket'])

products = {
    'clothing': [
        {'name': 'Майка', 'price': '100.00'},
        {'name': 'Штаны', 'price': '89.99'}
    ],
    'shoes': [
        {'name': 'Кроссовки', 'price': '190.00'},
        {'name': 'Ботинки', 'price': '150.00'}
    ],
    'jacket': [
        {'name': 'Куртка весенняя', 'price': '990.00'},
        {'name': 'Куртка зимняя', 'price': '1590.00'}
    ]
}


if __name__ == '__main__':
    app.run(debug=True)
