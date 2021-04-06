from flask import Flask, jsonify, request

app = Flask(__name__)
BookData = [ {
     "Id" : 1,
     "name" : "Xyz",
     "author" :"abc",
     "qty" : 3,
     "lcoation" : "selve 5"
        }
    ,
    {
     "Id" : 2,
     "name" : "LMN",
     "author" :"yui",
     "qty" : 2,
     "lcoation" : "selve 4"
        }
    ]
@app.route('/')
def index():
    return "flask homepage"

@app.route('/Books', methods=['GET','POST'])
def AddBook():
   if request.method == 'GET':
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
 

if __name__ == '__main__':
    app.run(debug=True)