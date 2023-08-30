import React from 'react'
import Logo from "../assets/rawdah.png"
import {Link } from "react-router-dom";
import "../styles/Navbar.css"
import ReorderIcon from '@mui/icons-material/Reorder';

function Navbar() {
  return (
    <div className='navbar'>
      <div className='leftside'>
        <img src={Logo} alt="Logo"/>
      </div>
      <div className='rightside'></div>
      <Link to="/">Home</Link>
      <Link to="/menu">Menu</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>
      <button>
      <ReorderIcon/>
      </button>
      
    </div>
  )
}

export default Navbar
