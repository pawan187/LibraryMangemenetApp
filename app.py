from flask import Flask, jsonify, request
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PHZPDSQLDB2K12;'
                      'Database=testfoript;'
                      "Uid=testiptdbo;"
                      "PWD=testiptdbo123;")

cursor = conn.cursor()


app = Flask(__name__)

@app.route('/')
def index():
    return "flask homepage"

@app.route('/Books', methods=['GET','POST'])
def AddBook():
   if request.method == 'GET':
       BookData = []
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
       print(data)
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
       members = []
       cursor.execute("SELECT * FROM [testfoript].[dbo].[LibraryMembers];") 
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
       count = cursor.execute("INSERT INTO [testfoript].[dbo].[LibraryMembers] ( Mname, contact, balance, address) VALUES (?,?,?,?)",data['Mname'], data['contact'],str(data['balance']),data['address'])
       cursor.commit()
       print(count)
       return data
@app.route('/members/<id>', methods=['PUT','DELETE'])
def EditMemebers(id):
   if request.method == 'PUT':
       data = request.json
       count = cursor.execute("update [dbo].[LibraryMembers]  set [Mname] = ?, contact = ?, balance = ?, address = ? where id = ?",data['name'], data['contact'],str(data['balance']),data['address'],id)
       cursor.commit()
       data = jsonify("edited")
       print(data)
       return data
   elif request.method == 'DELETE':
       count = cursor.execute("DELETE FROM [dbo].[LibraryMembers] WHERE id like '"+ id +"'")
       count.commit()
       data = jsonify("deleted!")
       print(count)
       return data
@app.route('/transaction', methods=['GET','POST'])
def AddTransaction():
   if request.method == 'GET':
       Transactions =[]
       cursor.execute("SELECT *  FROM [testfoript].[dbo].[LibraryTransactions]")
       row = cursor.fetchone()
       while row:
           Transactions.append({
               "id" : row[0],
               "Bid" : row[1],
               "Mid": row[2],
               "date":row[3],
               "status" : row[4]
               })
           row = cursor.fetchone()
       data = jsonify(Transactions)
       print(data)
       return data
   elif request.method == 'POST':
       data = request.json
       cursor.execute(" DECLARE @return_value int EXEC	@return_value = [dbo].[LibraryInsertTransaction] @Mid = ?, @Bid = ?, @TDate = ?, @Tstatus = ? SELECT	'Return Value' = @return_value ", data["Mid"] , data["Bid"], str(data["TDate"]), data["Tstatus"])
       cursor.commit()
       transaction.append(data)
       return data
@app.route('/transaction/<id>', methods=['PUT','DELETE'])
def EditTransaction(id):
   if request.method == 'PUT':
       data = request.json
       row = cursor.execute("SET NOCOUNT ON; declare @rc int; exec @rc = [dbo].[LibraryReturnTransaction] Bid= ?, Mid= ?,amount = ? select @rc as rc" , data["Bid"], data["Mid"] ,data["amount"])
       row.commit()
       data = jsonify(row)
       print(data)
       return data
   elif request.method == 'DELETE':
       row = row.execute("dalete from [testfoript].[dbo].[LibraryTransactions] where id - ? " , id)
       row.commit()
       data = jsonify(row)
       print(data)
       return data
 
if __name__ == '__main__':
    app.run(debug=True)