import React from 'react'
export default ()=>{
const Books=[{
    title:"titans",
    author:"pawan",
    qty:10,
    fees :50
}] 
return (
    <div>
        <h1>List of books</h1>
        <ul>
        {Books.map((element,key)=>{
            return(
                <li key={key}>
                   title: {element.title}
                </li>
            )
        })} 
        </ul>     
    </div>
)
}
