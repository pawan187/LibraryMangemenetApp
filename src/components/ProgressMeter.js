import React from 'react'
import {Progress } from 'semantic-ui-react'
export default ({title, value ,total})=>{
    return (
      <Progress inverted progress='value' total={total} value={value} >
      {title}
      </Progress>
    )
  }