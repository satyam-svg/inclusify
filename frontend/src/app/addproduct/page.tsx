import React from "react";
import "./addproduct.css";
import Navbar from "../../../Components/ui/Navbar/page";
import home from "./Image/icons8-home-24.png";
import Image from "next/image";
import Link from "next/link";
import menuicon from "./Image/menu.png";
import img1 from "./Image/img-1.png";
import img2 from "./Image/img-2.png";
import img3 from "./Image/img-4.png";
import add from "./Image/Group 107.png";
import Footer from '../../../Components/ui/Footer/page'
const page = () => {
  return (
    <>
      <div className="add_product">
        <div className="add_product_items">
          <Navbar />
          <div className="addproduct_menu">
            <Link href="/">
              <Image src={home} alt="loading-image" />
            </Link>
            <h1>/</h1>
           <Link href="/productlist"><h2>Product</h2></Link>
            <h3>/</h3>
            <h4>Add Product</h4>
          </div>
          <div className="heading_addproduct">
            <h1>Add Product</h1>
            <h2>Add your product for your customers</h2>
          </div>
          <div className="imformation_form">
            <div className="imformation_form_items">
              <div className="imformation_form_heading">
                <h1>Basic Imformation</h1>
                <Image
                  src={menuicon}
                  alt="loading-image"
                  className="menuicon"
                />
              </div>
              <div className="imformation_form_box">
                <div className="imformation_form_box_items">
                  <form action="/addproduct" method="post">
                    <label htmlFor="name">Input your Product Name</label>
                    <input type="text" placeholder="Oil" />
                    <label htmlFor="name">Input your Description Here</label>
                    <input
                      type="text"
                      className="description"
                      placeholder="Description here"
                    />
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div className="price_form">
            <div className="price_form_items">
              <div className="price_form_heading">
                <h1>Price</h1>
                <Image
                  src={menuicon}
                  alt="loading-image"
                  className="menuicon"
                />
              </div>
              <div className="price_form_box">
                <div className="price_form_box_items">
                  <form action="/addproduct" method="post">
                    <label htmlFor="name">Minimum Order</label>
                    <input type="text" placeholder="10,000" />
                    <label htmlFor="name">Unit Price</label>
                    <input type="text" placeholder="120" />
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div className="image_form">
            <div className="image_form_items">
              <div className="image_form_heading">
                <h1>Product Pictures</h1>
                <Image
                  src={menuicon}
                  alt="loading-image"
                  className="menuicon"
                />
              </div>
              <div className="image_form_box">
                <div className="image_form_box_items">
                  <Image src={img1} alt="loading-image" priority />
                  <Image src={img2} alt="loading-image" priority />
                  <Image src={img3} alt="loading-image" priority />
                  <Image src={add} alt="loading-image" priority />
                </div>
              </div>
            </div>
          </div>
          <div className="image_form">
            <div className="image_form_items">
              <div className="image_form_heading">
                <h1>Category</h1>
                <Image
                  src={menuicon}
                  alt="loading-image"
                  className="menuicon"
                />
              </div>
              <div className="image_form_box">
                <div className="image_form_box_items">
                  <form action="/addproduct" method="post">
                    <label htmlFor="name">Product category</label>
                    <input type="text" placeholder="Oil" />
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div className="button_addproduct">
              <button>Save Product</button>
          </div>
          <Footer/>
        </div>
      </div>
    </>
  );
};

export default page;
