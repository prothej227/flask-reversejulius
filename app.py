import flask
import os
from bruteforce import SolnSpace, Bruteforce
from flask import render_template, request, redirect, url_for, session

app = flask.Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST','GET'])
def caesarDecrypt():
    try:
        if request.method == "POST":
            strMsg = request.form["inputMsg"]
            session['myMsg'] = request.form["inputMsg"]
            lang = str(request.form["lang"])
            decryptMsg = str(SolnSpace(strMsg)[Bruteforce(SolnSpace(strMsg), lang)[0]])
            key = str(Bruteforce(SolnSpace(strMsg), lang)[0])
            refWord = str(Bruteforce(SolnSpace(strMsg), lang)[1]).upper()
            return render_template('index.html', outMsg = decryptMsg, key = key, strMsg = strMsg, refWord = refWord)
        else:
            return render_template('index.html', outMsg = decryptMsg, key = key, strMsg = strMsg, refWord = refWord)
    
    #For Debugging
    
    except Exception as e:
        return "<h1>Error Occured</h1><p>"+str(e)+"</p>"
    
    # except:
        # return redirect(url_for('index'))

@app.route('/solnspace/')
def showSolnSpace():
    strMsg = session.get('myMsg', None)
    listSoln = SolnSpace(strMsg)
    return render_template('layout.html', soln = listSoln, strMsg = strMsg)
    
if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')
    