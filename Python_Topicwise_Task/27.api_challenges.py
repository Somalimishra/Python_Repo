# 1.write a program to insert a record in sql table via api
# 2.write a program to update a record via api
# 3.write a program to delete a record via api
# 4.write a program to fetch a record via api
# 5.All the above questions you have to answer for mongo db as well

app= Flask(__name__)

mydb=conn.connect(host='localhost',user='root',passwd='1234')
cursor=mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.mysqltable(name varchar(30), number int)")
# 1.write a program to insert a record in sql table via api
@app.route('/insert',methods=['GET','POST'])
def insert():
    if (request.method == 'POST'):
        name=request.json['name']
        number=request.json['number']
        cursor.execute("insert into tasksql.mysqltable values (%s,%s)",(name,number))
        mydb.commit()
        return jsonify(str("successfully inserted"))
# 2.write a program to update a record via api
@app.route('/update', methods=['GET', 'POST'])
def update():
    if (request.method == 'POST'):
        name = request.json['name']
        cursor.execute("update tasksql.mysqltable set number=number+10 where name=%s", (name,))
        mydb.commit()
        return jsonify(str("successfully updated"))
# 3.write a program to delete a record via api
@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from tasksql.mysqltable where name=%s",(name_del,))
        mydb.commit()
        return jsonify(str("successfully deleted"))
# 4.write a program to fetch a record via api
@app.route('/fetch', methods=['POST','GET'])
def fetch():
    cursor.execute("select * from tasksql.mysqltable")
    l=[]
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

#This will invoke entire main class
if __name__=='__main__':
    app.run()