import React ,{useState} from 'react'
const SearchTransaction =()=>{
    const [text,setText] = useState('') 
    return(
      <form>
        <p>search text : {text}     </p>
        <input type='text' value={text} onChange={(e)=>{setText(e.target.value)}} ></input>
        <p> incomes only : <input type='checkbox'/></p>
      </form>
    )
  }
  export default SearchTransaction