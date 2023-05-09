from flask import Flask,render_template,jsonify
from flask import request
#flask creates a server
app = Flask(__name__)
#flask understands python
#website understands html,css and javascript
#hence heterogenous
@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')#renders html page

@app.route('/math',methods = ['POST'])
def math_operation():
    if(request.method=='POST'):
        ops=request.form['operation']
        num1=int(request.form['num1'])#instead of form we can use jsonify
        num2=int(request.form['num2'])
        if(ops=="add"):
            r=num1+num2
            result="the sum of"+str(num1)+"+"+str(num2)+"is"+str(r)
           
        if(ops=="subtract"):
            r=num1-num2
            result="the difference of"+str(num1)+"-"+str(num2)+"is"+str(r)
           
        if(ops=="multiply"):
            r=num1*num2
            result="the product of"+str(num1)+"*"+str(num2)+"is"+str(r)
           
        if(ops=="divide"):
            r=num1/num2
            result="the division of"+str(num1)+"/"+str(num2)+"is"+str(r)
        return render_template('results.html',result=result)
#to pass data through postman use 
#@app.route('/postman_data',methods = ['POST])
#ops=int(request.json['num1'])
        
        

# @app.route("/")#binding
# def hello_world():
#     return "<h1>Hello, World!</h1>"

# @app.route("/hello_world1")#binding
# def hello_world1():
#     return "<h1>Hello, World1!</h1>"

# @app.route("/hello_world2")#binding
# def hello_world2():
#     return "<h1>Hello, World2!</h1>"

# @app.route("/test")
# def test():
#     a=5+6
#     return "this is my function to run app {}".format(a)#to return 5+6 use format
# @app.route("/test2")
# def test2():
#     data=request.args.get('x')
#     #requests to get input    
#     return "this is the data input{}".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")#running
