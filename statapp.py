from flask import Flask, redirect, url_for, request
import math, statistics
app = Flask(__name__)

@app.after_request
def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain"
    return response

@app.route('/statapp/<userIn>')
def statapp(userIn):
    scores = userIn.split(",")
    for i in range(len(scores)):
        scores[i]=int(scores[i])

    mean = sum(scores) / len(scores)
    res = sum((x - mean) ** 2 for x in scores) / len(scores)
    sd = math.sqrt(res)
    median = statistics.median(scores)

    output = "You inputted " + userIn + "\n"
    output = output + "The mean of list is : " + str(mean) + "\n"
    output = output + "The variance of list is : " + str(res) + "\n"
    output = output + "The sd of list is : " + str(sd) + "\n"
    output = output + "The median of list is : " + str(median)
    return output 

@app.route('/tabulate', methods=['POST', 'GET'])
def tabulate():
    if request.method == 'POST':
        userIn = request.form['userIn']
        return redirect(url_for('statapp', userIn=userIn))
    else:
        userIn = request.args.get('userIn')
        return redirect(url_for('statapp', userIn=userIn))
 
if __name__ == '__main__':
    app.run(debug=True)
