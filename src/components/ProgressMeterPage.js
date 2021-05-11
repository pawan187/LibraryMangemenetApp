import React ,{useState,useContext} from 'react'
import appContext from '../context/appContext'
import ProgressMeter from './ProgressMeter'
export default ()=>{
    const { dataset } = useContext(appContext)
    const {income,expense} = dataset.stats
    const [stats , setStats] = useState([{
      title : 'Earnings',
      value : income,
      total : income
    },{
      title : 'Expense',
      value : expense,
      total : income
    }, {
      title : 'Saving',
      value : income-expense,
      total : income
    }])
    return (
      <div> 
            {
              stats.map((element)=>{
                return (<ProgressMeter 
                    key={element.title}
                    title = {element.title} 
                    value = {element.value} 
                    total={element.total}/>)
              }
            )
          }
      </div>
    )
  }