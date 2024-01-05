import React from "react";
import "./screen5.css";
import Image from "next/image";
import Poor from "./Image/woman-offering-food-neighbor.jpg";
import Arrow from "./Image/Arrow 1.png";
import tick from "./Image/Ok.png";
const page = () => {
  return (
    <>
      <div className="screen5">
        <div className="screen5-items">
          <div className="content_screen5">
            <div className="poor-image">
              <Image src={Poor} alt="women-image" className="poor" priority />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default page;
