import React from 'react'
import { RxHamburgerMenu } from "react-icons/rx";
import { IoBagOutline } from "react-icons/io5";
import { BsPerson } from "react-icons/bs";
import logo from "../Assets/logo.png";
import { NavLink } from 'react-router-dom';
import '../Assets/Styles/Navbar.css'

const Navbar = () => {
    return (
        <div className='navbarContainer rounded-xl bg-stone-100'>
            {/* <navbar className='mobileNav md:hidden'>
        <logo>
            <img src={logo} />
        </logo>
            <div className='rightNav flex flex-row  ml-auto'>
                <IoBagOutline />
                <BsPerson />
                <RxHamburgerMenu />
            </div>
        </navbar> */}
            <navbar className='fullNav md:flex flex-row px-2'>
                <div className='leftNav flex flex-row hidden md:flex md:items-center'>
                    <ul>
                        <NavLink to='/' className='navOptions'>
                            Home
                        </NavLink>
                        <NavLink to='/Shop' className='navOptions'>
                            Shop
                        </NavLink>
                        <NavLink to='/About' className='navOptions'>
                            About
                        </NavLink>
                        <NavLink to='/Contact' className='navOptions'>
                            Contact
                        </NavLink>
                    </ul>
                </div>
                <div className='flex logoContainer md:justify-center'>
                    <img src={logo} alt='logo' className='logo ml-auto md:flex md:ml-0' />
                </div>
                <div className='rightNav flex flex-row ml-auto items-center mr-2'>
                    <IoBagOutline className='rightIcons'/>
                    <BsPerson className='rightIcons'/>
                    <RxHamburgerMenu className='md:hidden rightIcons' />
                </div>
            </navbar>
        </div>
    )
}

export default Navbar