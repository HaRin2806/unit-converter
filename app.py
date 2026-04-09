from flask import Flask, render_template, request

app = Flask(__name__)

RATES = {
    'meter': 1.0,
    'kilometer': 1000.0,
    'centimeter': 0.01
}

@app.route('/', methods = ['GET', 'POST'])
def home():
    result = None
    
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        
        base_amount = amount * RATES[from_unit]
        converted_amount = base_amount / RATES[to_unit]
        
        result = f"{amount} {from_unit} = {converted_amount: .4f} {to_unit}"
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)