import React from 'react';
import './screen1.css';
import Women from './image/Screenshot 2023-12-28 230437.png';
import Image from 'next/image';
import Arrow from  './image/Arrow 1.png'
import Link from 'next/link'
import tick from './image/Ok.png'
const Page = () => {
  return (
    <div className="screen1">
      <div className="screen1-items">
        <div className="women-image">
          <Image
            src={Women}
            alt="women-image"
            className="stats"
            priority
          />
        </div>
        <div className="content">
          <h1>PROVIDE HOPE UNITE KINDNESS</h1>
          <h2>Unite goodness through the movement of zakat, charity, and benevolence. Together, let us share for those in need. </h2>
        </div>
        
      </div>
      <div className="button">
         <div className="button1">
           <h1>Get Started</h1>
         </div>
         <h2><Link href="/login"><u>Donation Process</u></Link></h2>
         <Image
         src={Arrow}
         alt='arrow-image'
         priority
         className='arrow'
         />
      </div> 
       <div className="label">
           <Image
             src={tick}
             alt='loading-image'
             className='tick'
           />
           <h1>Registered and directly supervised by the Supervisory Body</h1>
       </div>
    </div>
  );
};

export default Page;
