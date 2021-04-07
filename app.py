from flask import Flask, jsonify, request
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PHZPDSQLDB2K12;'
                      'Database=testfoript;'
                      "UID=testiptdbo;"
                      "PWD=testiptdbo123;")

cursor = conn.cursor()
cursor.execute('SELECT * FROM [testfoript].[Cure].[CureUser]')

for row in cursor:
    print(row)

app = Flask(__name__)
BookData = [ {
     "Id" : 1,
     "name" : "Xyz",
     "author" :"abc",
     "qty" : 3,
     "location" : "selve 5",
     "rent" : 10
        }
    ,
    {
     "Id" : 2,
     "name" : "LMN",
     "author" :"yui",
     "qty" : 2,
     "location" : "selve 4",
     "rent" : 15
        }
    ]
members = [{
    "Id" : 1,
    "name":"pawan",
    "contact":"7977763748",
    "balance" : 0
    }]

transaction = [
    {
        "Id" : 1,
        "BookId":1,
        "UserId":1,
        "date":"xyz"
}]
@app.route('/')
def index():
    return "flask homepage"

@app.route('/Books', methods=['GET','POST'])
def AddBook():
   if request.method == 'GET':
       cursor.execute("SELECT * FROM [testfoript].[dbo].[BooksLibrary];") 
       row = cursor.fetchone() 
       while row: 
           print(row[0])
           row = cursor.fetchone()
       data = jsonify(BookData)
       print(data)
       return data
   elif request.method == 'POST':
       data = request.json
       BookData.append(data)
       print(BookData)
       return data
@app.route('/Books/<id>', methods=['PUT','DELETE'])
def EditBook(id):
   if request.method == 'PUT':
       for i in range(0,len(BookData)):
           if BookData[i]["Id"] == int(id):
               print(request.args.get('name'))
               BookData[i]["name"] = request.args.get('name')
       data = jsonify(BookData)
       print(data)
       return data
   elif request.method == 'DELETE':
       for i in range(0,len(BookData)):
           print(BookData[i]["Id"]==int(id))
           if BookData[i]["Id"] == int(id):
               BookData.pop(i)
       data = jsonify(BookData)
       print(BookData)
       return data
 
@app.route('/memebers', methods=['GET','POST'])
def AddMemebers():
   if request.method == 'GET':
       data = jsonify(members)
       print(data)
       return data
   elif request.method == 'POST':
       data = request.json
       members.append(data)
       print(members)
       return data
@app.route('/memebers/<id>', methods=['PUT','DELETE'])
def EditMemebers(id):
   if request.method == 'PUT':
       for i in range(0,len(members)):
           if members[i]["Id"] == int(id):
               print(request.args.get('name'))
               members[i]["name"] = request.args.get('name')
       data = jsonify(members)
       print(data)
       return data
   elif request.method == 'DELETE':
       for i in range(0,len(members)):
           print(members[i]["Id"]==int(id))
           if members[i]["Id"] == int(id):
               members.pop(i)
       data = jsonify(members)
       print(members)
       return data
 
@app.route('/transaction', methods=['GET','POST'])
def AddTransaction():
   if request.method == 'GET':
       data = jsonify(transaction)
       print(data)
       return data
   elif request.method == 'POST':
       data = request.json
       transaction.append(data)
       print(transaction)
       return data
@app.route('/transaction/<id>', methods=['PUT','DELETE'])
def EditTransaction(id):
   if request.method == 'PUT':
       for i in range(0,len(transaction)):
           if transaction[i]["Id"] == int(id):
               print(request.args.get('date'))
               transaction[i]["date"] = request.args.get('date')
       data = jsonify(transaction)
       print(data)
       return data
   elif request.method == 'DELETE':
       for i in range(0,len(transaction)):
           print(transaction[i]["Id"]==int(id))
           if transaction[i]["Id"] == int(id):
               transaction.pop(i)
       data = jsonify(transaction)
       print(transaction)
       return data
 

if __name__ == '__main__':
    app.run(debug=True)