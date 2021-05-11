import React , {useState} from 'react'
import {Form } from 'semantic-ui-react'
class TransactionForm extends React.Component{
    state = {
        title : '',
        description : '',
        src : '',
        createdAt : 0,
        amount : 0,
        isIncome : false
    }
    render(){
        <div>
            <Form>
                <Form.Group>
                    <Form.Input label='title' value={this.state.title} onChange={(e)=>{
                        this.setState(()=>({title:e.target.value}))
                    }}/>
                    <Form.Input label='description'/>
                    <Form.Checkbox label='income transaction' />
                </Form.Group>
            </Form>
        </div>
    }
}