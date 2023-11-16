
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/ft2meters/<ft>')
def ft2meters(ft):
    meters = float(ft)/3.281
    output = 'Length entered is ' + str(ft)+ " feet and is " + str(meters) + " meters."
    return output 

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        userIn = request.form['ft']
        return redirect(url_for('ft2meters', ft=userIn))
    else:
        userIn = request.args.get('ft')
        return redirect(url_for('ft2meters', ft=userIn))
 
if __name__ == '__main__':
    app.run(debug=True)
