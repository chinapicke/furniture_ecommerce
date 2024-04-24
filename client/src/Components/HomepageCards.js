import React from 'react'
import { IoBagOutline } from "react-icons/io5";


const HomepageCards = ({ name, image, price, specialItem, colours }) => {
    return (
        <div className='cardContainer m-2 p-2 rounded-md'>
            <div className='cardUpper flex flex-row'>
                <button className='mr-auto'>{specialItem}</button>
                <p>{colours} Colours</p>
            </div>
            <img src={`data:image/jpeg;base64,${image}`} alt={name} />
            <div className='cardLower flex justify-between'>
                <div className='flex flex-col items-start'>
                    <h3>{name}</h3>
                    <h4>£{price}</h4>
                </div>
                <button><IoBagOutline /></button>
            </div>
        </div>
    )
}

export default HomepageCards