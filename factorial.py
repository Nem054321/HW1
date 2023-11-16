from flask import Flask, redirect, url_for, request
import math

app = Flask(__name__)

@app.route('/factorial/<num>')
def factorial(num):
    result = math.factorial(int(num))
    output = 'factorial(' + str(num)+ ") = " + str(result)
    return output

@app.route('/compute', methods=['POST', 'GET'])
def compute():
    if request.method == 'POST':
        userIn = request.form['num']
        return redirect(url_for('factorial', num=userIn))
    else:
        userIn = request.args.get('num')
        return redirect(url_for('factorial', num=userIn))
 
if __name__ == '__main__':
    app.run(debug=True)
