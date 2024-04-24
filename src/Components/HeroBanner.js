import React from 'react'
import Dropdown from './Dropdown'

const HeroBanner = () => {
    return (
        <div className='heroContainer my-5 flex flex-col '>
            <div className='sortBanner rounded-xl bg-slate-100 mt-auto mb-4 flex flex-col md:grid md:grid-cols-4 mx-3'>
                <div>
                    <h5>Made By</h5>
                    <Dropdown
                        showingOption='Wood'
                        options={[
                            'Fabric',
                            'Stainless Steel',
                            'Plastic',
                            'Glass',
                            'Rattan',
                        ]} />
                </div>
                <div>
                    <h5>Select Type</h5>
                    <Dropdown
                        showingOption='Sofa'
                        options={[
                            'Armchair',
                            'Table',
                            'Desk',
                            'Bed',
                            'Lamp',
                            'Wardrobe',
                            'Home Decor'
                        ]} />
                </div>
                <div>
                    <h5>Price</h5>
                    <Dropdown
                        showingOption='$150-$249'
                        options={[
                            'Under $50',
                            '$50-$149',
                            '$250-$349',
                            '$350-$449',
                            '$450-$549',
                            'Over $550'
                        ]} />
                </div>
                    <button className='rounded-xl searchBtn bg-zinc-800 text-slate-50 mx-2 mb-2 md:mx-0 md:mx-0'>Search</button>
            </div>
        </div>
    )
}

export default HeroBanner