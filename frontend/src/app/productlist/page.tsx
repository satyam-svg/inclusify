import React from "react";
import "./productlist.css";
import Navbar from "../../../Components/ui/Navbar/page";
import Image from "next/image";
import Link from "next/link";
import home from "./image/icons8-home-24.png";
import item from "./image/Rectangle 52.png";
import edit from "./image/edit.png";
import Footer from '../../../Components/ui/Footer/page'
const page = () => {
  return (
    <>
      <div className="product_list">
        <div className="product_list_items">
          <Navbar />
          <div className="addproduct_menu">
            <Link href="/">
              <Image src={home} alt="loading-image" />
            </Link>
            <h1>/</h1>
            <Link href="/productlist">
              <h2>Product</h2>
            </Link>
            <h3>/</h3>
            <Link href="/addproduct"><h4>Add Product</h4></Link>
          </div>
          <div className="heading_addproduct">
            <h1>My Product</h1>
            <h2>See the Product You have added </h2>
          </div>
          <div className="product_list_serial">
            <div className="box1_list">
              <div className="box_list_items">
                <Image src={item} alt="loading-image" priority />
                <div className="price_heading">
                  <h1>Quixing Oil</h1>
                  <h2>$400</h2>
                  <h3>Short Desciption lorem epsum dedo</h3>
                </div>
                <div className="date">
                  <h1>23/01/2022</h1>
                </div>
              </div>
              <div className="edit">
                <Image src={edit} alt="loading" priority />
              </div>
            </div>
            <div className="box1_list">
              <div className="box_list_items">
                <Image src={item} alt="loading-image" priority />
                <div className="price_heading">
                  <h1>Quixing Oil</h1>
                  <h2>$400</h2>
                  <h3>Short Desciption lorem epsum dedo</h3>
                </div>
                <div className="date">
                  <h1>23/01/2022</h1>
                </div>
              </div>
              <div className="edit">
                <Image src={edit} alt="loading" priority />
              </div>
            </div>
            <div className="box1_list">
              <div className="box_list_items">
                <Image src={item} alt="loading-image" priority />
                <div className="price_heading">
                  <h1>Quixing Oil</h1>
                  <h2>$400</h2>
                  <h3>Short Desciption lorem epsum dedo</h3>
                </div>
                <div className="date">
                  <h1>23/01/2022</h1>
                </div>
              </div>
              <div className="edit">
                <Image src={edit} alt="loading" priority />
              </div>
            </div>
            <div className="box1_list">
              <div className="box_list_items">
                <Image src={item} alt="loading-image" priority />
                <div className="price_heading">
                  <h1>Quixing Oil</h1>
                  <h2>$400</h2>
                  <h3>Short Desciption lorem epsum dedo</h3>
                </div>
                <div className="date">
                  <h1>23/01/2022</h1>
                </div>
              </div>
              <div className="edit">
                <Image src={edit} alt="loading" priority />
              </div>
            </div>
            <div className="box1_list">
              <div className="box_list_items">
                <Image src={item} alt="loading-image" priority />
                <div className="price_heading">
                  <h1>Quixing Oil</h1>
                  <h2>$400</h2>
                  <h3>Short Desciption lorem epsum dedo</h3>
                </div>
                <div className="date">
                  <h1>23/01/2022</h1>
                </div>
              </div>
              <div className="edit">
                <Image src={edit} alt="loading" priority />
              </div>
            </div>
            <div className="box1_list">
              <div className="box_list_items">
                <Image src={item} alt="loading-image" priority />
                <div className="price_heading">
                  <h1>Quixing Oil</h1>
                  <h2>$400</h2>
                  <h3>Short Desciption lorem epsum dedo</h3>
                </div>
                <div className="date">
                  <h1>23/01/2022</h1>
                </div>
              </div>
              <div className="edit">
                <Image src={edit} alt="loading" priority />
              </div>
            </div>
            

          </div>
          <div className="footer_list">
            <Footer/>   
            </div>
        </div>
      </div>
    </>
  );
};

export default page;
