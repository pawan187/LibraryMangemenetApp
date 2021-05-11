let express = require("express")
let app = express()
let cors = require('cors')
let path = require("path")
let bodyParser = require('body-parser')
app.use(express.static(path.resolve(__dirname,"..","build")))
// console.log(path.resolve(__dirname,"build"))
app.use(cors({
        "origin": "http://localhost:8000/",
        "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
        "preflightContinue": false,
        "optionsSuccessStatus": 204
      }
))
app.use(bodyParser.json())
app.listen(8000)
let notes = [{title : "eat" , body: "it is lunch time"}]
app.get('/',(req,res)=>{
    res.render('index.html')
})
app.get('/list',(req,res)=>{
    res.json(notes)
})
app.post('/list',(req,res)=>{
    console.log(req.body)
    let note = req.body.note
    notes.push(note)
    res.send('added successfully')
})
app.delete('/list',(req,res)=>{
    console.log(req.body)
    let elementodelete = req.body.elementtodelete;
    notes = notes.filter((element)=>element.title !==elementodelete)
    res.send("deletion successfull")
})