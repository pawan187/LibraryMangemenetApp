import ProgressForm from './ProgressForm'
import ProgressMeterPage from './ProgressMeterPage'
import BucketList from './BucketList'
import React , {useReducer} from 'react'
import transactionReducer from '../reducers/transactionReducer'
import appContext from '../context/appContext'
const App = ()=>{
  const [dataset,dispatch] =useReducer(transactionReducer,
    {
        filters : {
        month : 'jan',
        year : 2020
        },
        bucket : [
        {
            title : 'gas bill',
            amount : 850,
            description : 'paid for the lpg gas',
            imgSrc :'',
            isIncome : false,
            createdAt : 0
        },
        {
            title : 'salary',
            amount : 25000,
            description : 'paid by corporation',
            imgSrc :'',
            isIncome : true,
            createdAt : 50000
        }
        ],
        stats : {
        income : 25000,
        expense : 1650
        }
  })
  return (
    <appContext.Provider value={{dataset, dispatch}} >
        <div className="ui center aligned container">
            <p> stats of your money</p>
            <div>
            <ProgressForm />
            <ProgressMeterPage/>
            <div className='ui left aligned container'>
                <BucketList/>
            </div>
        </div> 
        </div>
    </appContext.Provider>
  )
}
export default App