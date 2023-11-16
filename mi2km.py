from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/mi2km/<mi>')
def mi2km(mi):
    km = float(mi) * 1.609
    output = 'Length entered is ' + str(mi)+ " mi and is " + str(km) + " km."
    return output 

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        userIn = request.form['mi']
        return redirect(url_for('mi2km', mi=userIn))
    else:
        userIn = request.args.get('mi')
        return redirect(url_for('mi2km', mi=userIn))
 
if __name__ == '__main__':
    app.run(debug=True)
