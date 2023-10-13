# # Import the Flask class from the flask module
# from flask import Flask

# # Create an instance of the Flask class, which will be our web application
# app = Flask(__name__)

# # Define a route for the root URL ("/") and the associated view function
# @app.route('/')
# def hello():
#     # This view function returns the text "Hello, World!" when accessed
#     return "Hello, World!!!!"

# # Define a route for the URL "/json" and the associated view function
# @app.route('/json')
# def json():
#     # This view function returns a JSON object with two key-value pairs
#     # "my_message" with value "cool", and "value" with value 10
#     return {"my_message": "cool", "value": 10}

# # Define a route for the URL "/html" and the associated view function
# @app.route('/html')
# def html():
#     # This view function returns an HTML string that displays a header with the text "You can also return HTML"
#     return "<h1>You can also return HTML</h1>"

# # This block of code is executed if the file is run as a script (not imported as a module)
# if __name__ == '__main__':
#     # Run the Flask web server with debugging mode turned on
#     app.run(debug=True)



# -----------------
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def fizzbuzz():
    numbers = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append('FizzBuzz')
        elif i % 3 == 0:
            numbers.append('Fizz')
        elif i % 5 == 0:
            numbers.append('Buzz')
        else:
            numbers.append(i)
    return render_template('fizzbuzz.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
