import React from 'react'
import { useState } from 'react'
import { IoIosArrowDown } from "react-icons/io";

const Dropdown = ({showingOption, options}) => {

    const [toggleIsOpen, setToggleIsOpen] = useState(false)

    const toggleDropdown = () => {
        setToggleIsOpen(current => !current)

    }


    return (
        <div className='dropdown'>
            <ul className='relative'>
                <div className='flex flex-row-reverse justify-center bg-white p-1 mb-2 border border-gray-900 border-2 rounded-lg mx-2' onClick={toggleDropdown}>
                <button > <IoIosArrowDown /></button>
                <li className='bg-white'>{showingOption}</li>
                </div>
                <div className='dropdownContainer flex justify-center'>
                {
                    toggleIsOpen ?
                        <div className='optionsDropDown flex flex-col absolute'>
                            {options.map((item)=>{
                                return(
                                    <>
                                    <li>{item}</li>
                                    </>
                                )
                            })}
                        </div>

                        : null
                }

                </div>
            </ul>
        </div>
    )
}

export default Dropdown