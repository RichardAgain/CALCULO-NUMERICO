from flask import Flask, render_template, url_for, request
from random import randint as rand
import potenciacion as po
import Interpolacion as intp
import random

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/unit_1', methods=["POST","GET"])
def unit_1():
    if request.method == "POST":
        size = request.form["size"]
        if size == "":
            return render_template("unit_1.html", size = 0)
        else:
            size = int(size)

        matriz = []
        for i in range(size):
            l = []
            for k in range(size):
                l.append(rand(1,100))
            matriz.append(l)

        
        x, y = po.main(matriz)

        return render_template("unit_1.html", size= int(size), matriz = matriz, valor = x, vector = y)
    else:
        return render_template("unit_1.html", size = 0)
    
@app.route('/unit_3', methods=['POST','GET'])
def unit_3():
    if request.method == "POST":
        size = request.form["size"]
        if size == "":
            return render_template("unit_3.html", size = 0)
        else:
            size = int(size)

        vector_1 = []
        vector_2 = []
        for i in range(size):
            vector_1.append(round(random.uniform(0, 7), 2))
            vector_2.append(round(random.uniform(0, 7), 2))
        
        try: 
            res = intp.main(vector_1, vector_2)
        except Exception as err:
            return render_template('error.html', url = 'unit_3', e = err)
    
        return render_template("unit_3.html", size = int(size), vectores = [vector_1, vector_2], res = res)
    else:
        return render_template("unit_3.html", size = 0)



if __name__ == "__main__":
    app.run(debug=True)