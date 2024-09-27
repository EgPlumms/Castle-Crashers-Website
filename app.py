from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html')

@app.route("/RK")
def Red_knight():
    return render_template('RK.html')

@app.route("/BK")
def Blue_Knight():
    return render_template('BK.html')

@app.route("/OK")
def Orange_knight():
    return render_template ('OK.html')

@app.route("/GK")
def Green_Knight():
    return render_template ('GK.html')

@app.route("/PC")
def Playable_Characters():
    return render_template('PC.html')

@app.route("/BS")
def BlackSmith():
    return render_template('BS.html')

@app.route("/PK")
def Pink_Knight():
    return render_template('PK.html')

@app.route("/GreyK")
def Grey_Knight():
    return render_template('GreyK.html')

@app.route('/Hatty')
def Hatty():
    return render_template('HT.html')

if __name__ == "__main__":
    app.run()