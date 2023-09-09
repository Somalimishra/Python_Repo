#API(platform indepenedent)
#API is jut a rules
#when we try to comunicate between two other system or platform which has been developed in two different
#language at that situation we try to use something which is called Protocol. There is 'http' and 'https' protocols
#Flask module you expose you function into outer world
#404: Restart the server
#500:
#200:

from flask import Flask, request, jsonify

#Object i have created for class Flask
app = Flask(__name__)

#@app: @ is just an annotation says right after this line"@app.route('/abc',methods=['GET','POST'])"
# call the function
#'/abc': creating the url
@app.route('/abc',methods=['GET','POST'])   #the entire line is used as a decorator
# GET: Getting a data through URL
# POST: Posting a data through URL
def test1():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify((str(result)))
        #jsonify means to return the result in default json format
@app.route('/abc1/som',methods=['GET','POST'])
def test2():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a*b
        return jsonify((str(result)))
@app.route('/abc2/som',methods=['GET','POST'])
def test3():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a-b
        return jsonify((str(result)))
@app.route('/abc22',methods=['GET','POST'])
def test4():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a/b
        return jsonify((str(result)))

@app.route('/abc5/som',methods=['GET','POST'])
def test5():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a**b
        return jsonify((str(result)))

#This will invoke entire main class
if __name__=='__main__':
    app.run()

# 1.write a program to insert a record in sql table via api
# 2.write a program to update a record via api
# 3.write a program to delete a record via api
# 4.write a program to fetch a record via api
# 5.All the above questions you have to answer for mongo db as well
