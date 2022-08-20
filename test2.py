from flask import Flask , request ,jsonify


app =Flask(__name__)

@app.route('/aksh',methods=['GET','POST'])
def test1():
    if(request.method=='POST'):
        import mysql.connector as connection
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
        import mysql.connector as connection
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
        import mysql.connector as connection
        mydb = connection.connect(host="localhost", database='Attribute_DataSet1', user="root", passwd="1234",
                                  use_pure=True)

        query = request.json['c']
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.close()
        result =print("Table Created!!")
        return jsonify((str(result)))

@app.route('aksh/datatable/call', methods=["GET","POST"])



if __name__=='__main__':
    app.run()