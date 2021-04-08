from flask import Flask, jsonify, request
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PHZPDSQLDB2K12;'
                      'Database=testfoript;'
                      "Uid=testiptdbo;"
                      "PWD=testiptdbo123;")

cursor = conn.cursor()
#cursor.execute('SELECT * FROM [testfoript].[Cure].[CureUser]')

#for row in cursor:
#    print(row)

app = Flask(__name__)
BookData = []
members = []

transaction = [
    {
        "id" : 1,
        "Bookid":1,
        "Userid":1,
        "date":"xyz"
}]
@app.route('/')
def index():
    return "flask homepage"

@app.route('/Books', methods=['GET','POST'])
def AddBook():
   if request.method == 'GET':
       BootData = []
       cursor.execute("SELECT * FROM [testfoript].[dbo].[LibararyBooks];") 
       row = cursor.fetchone() 
       while row: 
           BookData.append(
           {
            "id" : row[0],
            "name" : row[1],
            "author" :row[2],
            "charge": row[3],
            "location" : row[4],
            "qty" : row[5]
            })
           row = cursor.fetchone()
       data = jsonify(BookData)
       print(data)
       return data
   elif request.method == 'POST':
       data = request.json
       count = cursor.execute("INSERT INTO [testfoript].[dbo].[LibararyBooks] (name, author,charge, qty, location) VALUES (?,?,?,?,?)",data['name'] , data['author'],data['charge'] ,data['qty'],data['location'])
       cursor.commit()
       print(BookData)
       return data
@app.route('/Books/<id>', methods=['PUT','DELETE'])
def EditBook(id):
   if request.method == 'PUT':
       data = request.json
       query = cursor.execute("UPDATE [dbo].[LibararyBooks]    SET [name] = ?      ,[author] = ?,[charge] = ?,[location] = ?,[qty] = ? WHERE id = ? ",data['name'] , data['author'],data['charge'] ,data['location'],data['qty'],id)
       cursor.commit()
       data = jsonify("successfull")
       print(data)
       return data
   elif request.method == 'DELETE':
       count = cursor.execute("DELETE FROM [dbo].[LibararyBooks] WHERE id like '"+ id +"'")
       count.commit()
       data = jsonify("done")
       print(BookData)
       return data
 
@app.route('/members', methods=['GET','POST'])
def AddMemebers():
   if request.method == 'GET':
       cursor.execute("SELECT * FROM [testfoript].[dbo].[MembersLibrary];") 
       row = cursor.fetchone() 
       while row: 
           members.append(
           {
            "id" : row[0]
      ,"Mname" :row[1]
      ,"contact" :row[2]
      ,"balance" : row[3]
      ,"address" : row[4]
            })
           row = cursor.fetchone()
       data = jsonify(members)
       print(data)
       return data
   elif request.method == 'POST':
       data = request.json
       count = cursor.execute("INSERT INTO [testfoript].[dbo].[MembersLibrary] (id, Mname, contact, balance, address) VALUES (?,?,?,?,?)",data['id'],data['name'], data['contact'],str(data['balance']),data['address'])
       cursor.commit()
       print(members)
       return data
@app.route('/members/<id>', methods=['PUT','DELETE'])
def EditMemebers(id):
   if request.method == 'PUT':
       for i in range(0,len(members)):
           if members[i]["id"] == int(id):
               print(request.args.get('name'))
               members[i]["name"] = request.args.get('name')
       data = jsonify(members)
       print(data)
       return data
   elif request.method == 'DELETE':
       for i in range(0,len(members)):
           print(members[i]["id"]==int(id))
           if members[i]["id"] == int(id):
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
           if transaction[i]["id"] == int(id):
               print(request.args.get('date'))
               transaction[i]["date"] = request.args.get('date')
       data = jsonify(transaction)
       print(data)
       return data
   elif request.method == 'DELETE':
       for i in range(0,len(transaction)):
           print(transaction[i]["id"]==int(id))
           if transaction[i]["id"] == int(id):
               transaction.pop(i)
       data = jsonify(transaction)
       print(transaction)
       return data
 

if __name__ == '__main__':
    app.run(debug=True)