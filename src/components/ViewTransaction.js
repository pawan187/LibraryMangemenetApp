import React from 'react'
export default ()=>{
    const li = [0,1,2,3,4,5]
    return (
    <div className="container">
    <h3>View transaction page
    </h3>
    <ul className="list-group">
        {   li.map((item,key)=>{
                return ( <li className="list-group-item" key={key}> <a href='/trasaction:'{...item.toString()}>{item}</a> </li>)
            }) 
        }
        </ul>
    </div>
)}