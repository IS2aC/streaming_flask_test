from flask import Flask
from flask import render_template, jsonify



app = Flask(__name__)

# Route qui renvoie un élément JSON

@app.route('/data')
def data_test():
     #modification
     data ={"value":666}
     return dict(data)

# Route pour la page HTML
@app.route('/')
def test():
    donnees =  data_test()
    donnees =  donnees.get('value')
    return render_template('test.html', dt =  donnees)



if __name__ == "__main__":
     app.run(debug  = True)