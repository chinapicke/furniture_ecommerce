import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Components/Navbar';

const Shop = () => {

  const [products, setProducts] = useState([])

  const fetchAPI = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/products')
      const data = response.data;
      setProducts(data)
      console.log(data)
    }
    catch (err) {
      console.log(err.message)
    }
  }

  useEffect(() => {
    fetchAPI()
  }, [])
  return (
    <div>
      <Navbar />
    {products && products.map((item, index) => (
      <div key={index}>
        <h1>{item.name}</h1>
        <h1>{item.type}</h1>
        <img src={item.images[0]} alt={item.name} style={{ width: '100%', maxWidth: '600px', height: 'auto' }} />




      </div>
    ))}
  </div>
)
}

export default Shop