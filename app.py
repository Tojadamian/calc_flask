from flask import Flask, request, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
