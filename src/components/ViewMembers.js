import React from 'react'
export default ()=>{
    const books = [{
        "name":"titans",
        "author":"pawan",
        "charge": 50,
        "quantity":5,
        "location": "5th shelve"
    },{
        "name":"Meluha",
        "author":"ramesh",
        "charge": 150,
        "quantity":6,
        "location": "5th shelve"
    }
]
return (
    <div>
        <h1>LIst of Members</h1>
        
        <div class="row">
        {
        books.map((element ,key) => {
           return  (
            <div class="col-sm-6 col-md-4" key={key}>
            <div class="thumbnail">
              <img src="..." alt="..."></img>
              <div class="caption">
                <h3>Name : {element.name}</h3>
                <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
              </div>
            </div>
          </div>
           )
        })
    
        }
      </div>
    </div>
)
}
