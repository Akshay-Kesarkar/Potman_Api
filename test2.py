from flask import Flask , request ,jsonify


app =Flask(__name__)

@app.route('/aksh',methods=['GET','POST'])
def test1():
    if(request.method=='POST'):
        import mysql12.connector as connection
        mydb = connection.connect(host="localhost", user="root", passwd="1234", use_pure=True)

        query = request.json['a']
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.close()
        result =print("Database Created!!")
        return jsonify((str(result)))

@app.route('/aksh/datatable',methods=['GET','POST'])
def test2():
    if(request.method=='POST'):
        import mysql12.connector as connection
        mydb = connection.connect(host="localhost", database='Attribute_DataSet1', user="root", passwd="1234",
                                  use_pure=True)

        query = request.json['b']
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.close()
        result =print("data inserted")
        return jsonify((str(result)))

@app.route('/aksh/datatable/insert',methods=['GET','POST'])
def test3():
    if(request.method=='POST'):
        import mysql12.connector as connection
        mydb = connection.connect(host="localhost", database='Attribute_DataSet1', user="root", passwd="1234",
                                  use_pure=True)

        query = request.json['c']
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.close()
        result =print("Table Created!!")
        return jsonify((str(result)))

@app.route('/aksh/datatable/call', methods=["GET","POST"])
def test4():
    if(request.method=='POST'):
        import mysql12.connector as connection
        import sqlalchemy
        import mysql12
        import pymysql
        import pandas as pd
        mydb = connection.connect(host="localhost", database='Attribute_DataSet1', user="root", passwd="1234",
                                  use_pure=True)

        cursor = mydb.cursor()
        mydb.close()
        engine1 = request.json['d']
        engine = sqlalchemy.create_engine(engine1)
        data1 = pd.read_sql_table('attribute_dataset', engine)
        result = data1
        return jsonify(result)



if __name__=='__main__':
    app.run()