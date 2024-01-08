import React from "react";
import "./login.css";
import home from "./Image/Group 21.png";
import Link from "next/link";
import Image from "next/image";
import Email from "./Image/Envelope.png";
import Pass from "./Image/Screenshot 2024-01-07 210214.png";
import Google from "./Image/Google.png";
const page = () => {
  return (
    <>
      <div className="login">
        <div className="login_items">
          <div className="icon_login">
            <Image src={home} alt="loading-image" />
          </div>
          <div className="heading_login">
            <h1>Acess Your Account</h1>
          </div>
          <div className="form">
            <form action="/login" method="post">
              <input type="email" placeholder="Email" />
              <div className="email-icon">
                <Image src={Email} alt="Email-icon" />
              </div>
              <input type="Password" placeholder="Password" />
              <div className="pass-icon">
                <Image src={Pass} alt="pass-icon" />
              </div>
              <button>Sign in</button>
            </form>
            <div className="google">
              <h1>-or sign in with-</h1>
              <button>
                <Image src={Google} alt="loading-image" />
                <h1>Sign in with google</h1>
              </button>
            </div>
          </div>
        </div>
        <div className="signup">
          <h1>Don't have an account?</h1>
          <Link href="/signup"><h2>Sign up</h2></Link> 
        </div>
      </div>
    </>
  );
};

export default page;
