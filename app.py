from os import name
from flask import Flask,request
from werkzeug.utils import redirect
from flask.templating import render_template

app=Flask(__name__)
reall=[3,2,2,4,1,4,4,4,4,2,4,2,1,2,1,3,4,3,4,4,4,1,4,1,3,4,1,3,3,1,3,4,1,3,3,1,3,1,4,4,1,4,4,2,3,2,1,1,2,4,4,3,3,3,3]
optl=[]
marks=0
print(len(reall))

@app.route('/')
def startup():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def homepage():
    global optl,marks
    optl=[]
    for i in range(1,56):
        answer=request.form['answer'+str(i)]
        if answer=='a':
            answer=1
        elif answer=='b':
            answer=2
        elif answer=='c':
            answer=3
        elif answer=='d':
            answer=4
        elif answer=='e':
            answer=None
        optl.append(answer)
    for j in range(0,55):
        if reall[j]==optl[j]:
            marks=0.78+marks
        else:
            pass

    return render_template('thank.html',marks=marks)

if __name__=='__main__':
    app.run(debug=True)

