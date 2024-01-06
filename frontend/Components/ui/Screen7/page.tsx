import React from 'react'
import Image from 'next/image'
import './screen7.css'
import tick from './Image/Ok.png'
import Arrow from './Image/Arrow 1.png'
import Lawyer from './Image/front-view-smiley-judge-robe-holding-wooden-gavel.jpg'
const page = () => {
  return (
    <>
      <div className="screen7">
        <div className="screen7-items">
          <div className="poor-image">
            <Image src={Lawyer} alt="poor-image" className="lawyer" priority />
          </div>
          <div className="main_content">
            <h1>Accessible Justice, Bridging Gaps</h1>
            <h2>
            We bridge the gap for the underserved, providing accessible assistance to safeguard rights and seek justice.{" "}
            </h2>
          </div>
          
        </div>
        <div className="screen7_button">
         <div className="screen7_button1">
         <h2><u>Hire Lawyer</u></h2>
         <Image
         src={Arrow}
         alt='arrow-image'
         priority
         className='arrow'
         />
         </div>
         <h2 className="upload"><u>Read Guidelines</u></h2>
         <Image
         src={Arrow}
         alt='arrow-image'
         priority
         className='arrow'
         />
      </div> 
      <div className="screen7_label">
           <Image
             src={tick}
             alt='loading-image'
             className='screen7_tick'
           />
           <h1>Financial constraints? We offer accessible legal aid with loans.</h1>
       </div>
      </div>
    </>
  )
}

export default page
