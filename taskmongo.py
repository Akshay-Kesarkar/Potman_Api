from flask import Flask , request ,jsonify
import pymongo

app= Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://akshay:12345@cluster0.8prah.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['taskdb']
collcetion = database["taskcollection"]

@app.route("/insert/mongo", methods= ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collcetion.insert_one({name:number})
        return jsonify(str("succesfully inserted"))

@app.route("/update/mongo", methods=['POST'])
def update():
    if request.method == 'POST':
        name = request.json['name']
        number= request.json['number']
        myquery = {name:number}
        number1 = request.json['number1']
        newvalues = {"$set": {name: number1}}

        collcetion.update_one(myquery,newvalues)

        return jsonify(str("succesfully inserted"))

if __name__=='__main__':
    app.run(port= 5004)
