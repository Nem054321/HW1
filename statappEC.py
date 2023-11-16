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
    hist0 = "__0"
    hist10 = "_10"
    hist20 = "_20"
    hist30 = "_30"
    hist40 = "_40"
    hist50 = "_50"
    hist60 = "_60"
    hist70 = "_70"
    hist80 = "_80"
    hist90 = "_90"
    hist100 = "100"

    for i in range(len(scores)):
        scores[i]=int(scores[i])
        if scores[i] >= 100:
            hist100 = hist100 + "*"
        elif scores[i] >= 90:
            hist90 = hist90 + "*"
        elif scores[i] >= 80:
            hist80 = hist80 + "*"
        elif scores[i] >= 70:
            hist70 = hist70 + "*"
        elif scores[i] >= 60:
            hist60 = hist60 + "*"
        elif scores[i] >= 50:
            hist50 = hist50 + "*"
        elif scores[i] >= 40:
            hist40 = hist40 + "*"
        elif scores[i] >= 30:
            hist30 = hist30 + "*"
        elif scores[i] >= 20:
            hist20 = hist20 + "*"
        elif scores[i] >= 10:
            hist10 = hist10 + "*"                        
        else:
            hist0 = hist0 + "*"                        

    mean = sum(scores) / len(scores)
    res = sum((x - mean) ** 2 for x in scores) / len(scores)
    sd = math.sqrt(res)

    output = "You inputted " + userIn + "\n\n"
    output = output + "The mean of list is : " + str(mean) + "\n"
    output = output + "The variance of list is : " + str(res) + "\n"
    output = output + "The sd of list is : " + str(sd) + "\n\n"
    output = output + hist0 + "\n"
    output = output + hist10 + "\n"
    output = output + hist20 + "\n"
    output = output + hist30 + "\n"
    output = output + hist40 + "\n"
    output = output + hist50 + "\n"
    output = output + hist60 + "\n"
    output = output + hist70 + "\n"
    output = output + hist80 + "\n"
    output = output + hist90 + "\n"
    output = output + hist100
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
