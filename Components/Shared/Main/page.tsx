import React from 'react'
import './main.css'
import Navbar from '../../ui/Navbar/page'
import Screen1 from '../../ui/Screen1/page'
import Screen2 from '../../ui/Screen2/page'
import Screen3 from '../../ui/Screen3/page'
const page = () => {
  return (
    <>
    <div className="container">
    <Navbar/>
     <Screen1/>
     <Screen2/>
     <Screen3/>
    </div>
         

    </>
  )
}

export default page
