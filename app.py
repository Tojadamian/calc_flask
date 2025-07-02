from flask import Flask, jsonify, request, render_template
import currency

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['num1'])
            operation = request.form['operation']
            if operation == 'sqrt':
                if a < 0:
                    result = "Cannot take square root of a negative number"
                else:
                    result = a ** 0.5
            else:
                b = float(request.form['num2'])
                if operation == 'add':
                    result = a + b
                elif operation == 'subtract':
                    result = a - b
                elif operation == 'multiply':
                    result = a * b
                elif operation == 'divide':
                    if b == 0:
                        result = "Error: Division by zero"
                    else:
                        result = a / b
                elif operation == 'power':
                    result = a ** b
        except (ValueError, ZeroDivisionError) as e:
            result = "Error: " + str(e)
    return render_template('calculator.html', result=result)

# Uncomment the following lines if you want to use the API endpoints
# Now they are commented out to avoid confusion with the calculator and currency conversion functionality.
# Unused API endpoints for currencies and exchange rates
# Only for demonstration purposes, not used in the current application.
# 
# @app.route('/api/currencies', methods=['GET'])
# def api_currencies():
#     currencies = currency.get_all_currencies_code()
#     return jsonify({"currencies": currencies})

# @app.route('/api/exchange_rate', methods=['GET'])
# def api_exchange_rate():
#     tab = request.args.get('tab')
#     code = request.args.get('code')
#     if not tab or not code:
#         return jsonify({"error": "Missing parameters"}), 400
#     rate = currency.get_exchange_rate(tab, code)
#     if rate is None:
#         return jsonify({"error": "Invalid tab or code"}), 404
#     return jsonify({"rate": rate})

@app.route('/currencies', methods=['GET'])
def currencies():
    return render_template('currencies.html')

@app.route('/api/search-currencies', methods=['GET'])
def search_currencies():
    query = request.args.get('q', '').upper()
    codes = currency.get_all_currencies_code()
    # Możesz rozbudować o wyszukiwanie po nazwach, jeśli je masz
    matches = [code for code in codes if query in code]
    return jsonify(matches)

@app.route('/api/convert-currency', methods=['POST'])
def api_convert_currency():
    try:
        amount = float(request.form['amount'])
        from_code = request.form['from_currency'].upper()
        to_code = request.form['to_currency'].upper()
        result = currency.convert_currency(amount, from_code, to_code)
        if result is None:
            return jsonify({"error": "Invalid currency code"}), 400
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
