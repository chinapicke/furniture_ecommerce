import Navbar from '../Components/Navbar'
import HeroBanner from '../Components/HeroBanner'
import '../Assets/Styles/Landing.css'
import { useEffect, useState } from 'react'
import axios from 'axios'
import HomepageCards from '../Components/HomepageCards'

const Landing = () => {

  const [homepageProducts, setHomepageProducts] = useState([]);
  const [specialProducts, setSpecialProducts] = useState();


  useEffect(() => {

    const fetchAPI = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:5000/products')
        const data = res.data
        setHomepageProducts(data)
        // data.map((item)=>{
        //   if (item.id === 109 || item.id === 107 || item.id === 104 || item.id === 103 || item.id === 102 || item.id === 101){
        //     setHomepageProducts(current =>[...current, item])
        //   }
        // if (item.id === 109 || item.id === 107 || item.id === 104 || item.id === 103 || item.id === 102 || item.id === 101){
        //   emptyArr.push(item)
        // }
        // setHomepageProducts.push(emptyArr)
        // })

      }
      catch (err) {
        console.log(err.message)
      }
    };


    fetchAPI();

  }, [])

  // Filter homepageProducts when it's updated
  useEffect(() => {
    const filteredArray = homepageProducts.filter((item) => item.id === 109 || item.id === 107 || item.id === 104 || item.id === 103 || item.id === 102 || item.id === 101);
    setSpecialProducts(filteredArray);
  }, [homepageProducts]);

  // useEffect(() => {

  //   });
  // }, [homepageProducts]);


  return (
    <div className='m-3'>
      <Navbar />
      <HeroBanner />
      <div className='homepageCard grid grid-cols-1 md:grid-cols-3'>
          {
          specialProducts && specialProducts.map((item) => {
            return (
              <>
                <HomepageCards
                  name={item.name}
                  price={item.price}
                  image={item.image_data}
                  specialItem={
                    item.id === 102 ? 'Top Rated' : 'Best Price'
                  }
                  colours={item.colours}
                />
              </>
            )
          })


        } 
      </div>

    </div>
  )
}

export default Landing