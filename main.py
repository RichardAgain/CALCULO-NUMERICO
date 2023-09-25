from flask import Flask, render_template, url_for, request
from random import randint as rand
import potenciacion as po
import Interpolacion as intp

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
    
@app.route('/unit_2', methods=['POST','GET'])
def unit_2():
    if request.method == "POST":
        size = request.form["size"]
        if size == "":
            return render_template("unit_2.html", size = 0)
        else:
            size = int(size)

        vector_1 = []
        vector_2 = []
        for i in range(size):
            vector_1.append(rand(1,20))
            vector_2.append(rand(1,20))
        
        res = intp.main(vector_1, vector_2)
    
        return render_template("unit_2.html", size = int(size), vectores = [vector_1, vector_2], res = res)
    else:
        return render_template("unit_2.html", size = 0)



if __name__ == "__main__":
    app.run(debug=True)