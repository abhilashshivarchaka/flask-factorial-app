from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['number'])  # Get input number
            result = factorial(num)  # Calculate the factorial
        except ValueError:
            result = "Please enter a valid number."  # Error if input is not a valid number
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

