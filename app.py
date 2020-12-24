import flask
import os
from bruteforce import SolnSpace, Bruteforce
from flask import render_template, request, redirect, url_for, session

app = flask.Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/', methods=['POST','GET'])
def index():
    # Set en_us as default language:
    lang = "en_us"
    try:
        if request.method == "POST":
            strMsg = request.form["inputMsg"]
            session['myMsg'] = request.form["inputMsg"]
            lang = str(request.form["lang"])
            decryptMsg = str(SolnSpace(strMsg)[Bruteforce(SolnSpace(strMsg), lang)[0]])
            key = str(Bruteforce(SolnSpace(strMsg), lang)[0])
            refWord = str(Bruteforce(SolnSpace(strMsg), lang)[1]).upper()
            
            # Retain Selected after Submit
            if lang == "en_us":
                lang_selected_us = "selected"
                lang_selected_tl = ""
            else:
                lang_selected_us = ""
                lang_selected_tl = "selected"               
            return render_template('index.html', outMsg = decryptMsg, key = key, strMsg = strMsg, refWord = refWord, lang_selected_us = lang_selected_us, lang_selected_tl = lang_selected_tl)
  
    #For Debugging
    except Exception as e:
        return "<h1>Error Occured</h1><p>"+str(e)+"</p>"
    #except:
        # return redirect(url_for('index'))
    return render_template('index.html') or redirect(url_for('index'))

@app.route('/solnspace/key/<int:keySoln>')
def showSolnSpace(keySoln):
    strMsg = session.get('myMsg', None)
    listSoln = SolnSpace(strMsg)
    return render_template('layout.html', soln = listSoln, strMsg = strMsg, key = keySoln)
    
if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')
    