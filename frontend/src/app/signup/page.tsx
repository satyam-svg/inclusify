"use client";
import React, { useState } from "react";
import "./signup.css";
import home from "./Image/Group 21.png";
import Link from "next/link";
import Image from "next/image";
import Email from "./Image/Envelope.png";
import Pass from "./Image/Screenshot 2024-01-07 210214.png";
import Google from "./Image/Google.png";
import { useRouter } from "next/navigation";
import axios from "axios";
import { toast } from "react-hot-toast";

export default function Signup() {
  const router = useRouter();
  const [user, setUser] = useState({
    email: "",
    password: "",
    confirmpassword: "",
  });
  const [loading, setLoading] = useState(false);

  const onSignup = async () => {
    try {
      console.log("Signup button clicked");
  
      // Check if password and confirm password match
      if (user.password !== user.confirmpassword) {
        toast.error("Password and Confirm Password do not match");
        return;
      }
  
      setLoading(true);
      const response = await axios.post(
        "http://127.0.0.1:8000/accounts/sign-up/",
        user
      );
      console.log("Signup success", response.data);
  
      // Only navigate to login page if signup is successful
      router.push("/login");
    } catch (error) {
      console.log("Signup failed", error);
  
      // Log the detailed error response
      if (error.response) {
        console.log("Error response:", error.response.data);
      }
  
      toast.error("Signup failed. Please check the console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="signup">
        <div className="signup_items">
          <div className="icon_signup">
            <Image src={home} alt="loading-image" />
          </div>
          <div className="heading_signup">
            <h1>Access Your Account</h1>
          </div>
          <div className="form">
            <form>
              <input
                type="email"
                placeholder="Email"
                name="email"
                onChange={(e) =>
                  setUser({ ...user, email: e.target.value })
                }
              />
              <div className="email-icon">
                <Image src={Email} alt="Email-icon" />
              </div>
              <input
                type="password"
                placeholder="Password"
                name="password"
                onChange={(e) =>
                  setUser({ ...user, password: e.target.value })
                }
              />
              <div className="pass-icon">
                <Image src={Pass} alt="pass-icon" />
              </div>
              <input
                type="password"
                placeholder="Confirm-Password"
                name="confirmpassword"
                onChange={(e) =>
                  setUser({ ...user, confirmpassword: e.target.value })
                }
              />
              <div className="con_pass-icon">
                <Image src={Pass} alt="pass-icon" />
              </div>
              <button  onClick={onSignup} type="button">Sign up</button>
            </form>
            <div className="google">
              <h1>-or sign in with-</h1>
              <button>
                <Image src={Google} alt="loading-image" />
                <h1>Sign up with google</h1>
              </button>
            </div>
          </div>
        </div>
        <div className="login_to">
          <h1> Already have an account?</h1>
          <Link href="/login">
            <h2>Login</h2>
          </Link>
        </div>
      </div>
    </>
  );
}
