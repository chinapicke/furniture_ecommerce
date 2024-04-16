from flask import Flask, jsonify
from flask_cors import CORS
from db_utils import get_products
import base64




app=Flask(__name__)
CORS(app)

products = [
    {
        'id':101,
        'name':'Basic Sofa', 
        'type':'Sofa',
        'material':'Fabric',
        'images':['data:image/png;base64,{}'.format(base64.b64encode(open('creamSofa.png', 'rb').read()).decode()), 'https://www.ikea.com/us/en/images/products/linanaes-loveseat-vissle-beige__0985924_pe816903_s5.jpg?f=xl'],
        # 'images':['https://www.ikea.com/us/en/images/products/linanaes-loveseat-vissle-beige__0972125_pe811545_s5.jpg?f=xxl','https://www.ikea.com/us/en/images/products/linanaes-loveseat-vissle-beige__0985924_pe816903_s5.jpg?f=xl' ],
        'price':524.79,
        'colours':6
    }, 
        {
        'id':102,
        'name':'Glass Lamp', 
        'type':'Lamp',
        'material':'Glass',
                'images':['data:image/png;base64,{}'.format(base64.b64encode(open('lamp.png', 'rb').read()).decode()), 'https://www.ikea.com/us/en/images/products/pilblixt-table-lamp-white-light-green-glass-gold-effect-metal__1132171_pe878166_s5.jpg?f=xl'],

        # 'images':['https://www.ikea.com/us/en/images/products/pilblixt-table-lamp-white-light-green-glass-gold-effect-metal__1132176_pe878168_s5.jpg?f=xl', 'https://www.ikea.com/us/en/images/products/pilblixt-table-lamp-white-light-green-glass-gold-effect-metal__1132171_pe878166_s5.jpg?f=xl'],
        'price':99.75,
        'colours':2


    }, 
        {
        'id':103,
        'name':'Glass Vase', 
        'type':'Home_Decor',
        'material':'Glass',
                'images':['data:image/png;base64,{}'.format(base64.b64encode(open('greenVase.png', 'rb').read()).decode()), 'https://www.ikea.com/fr/fr/images/products/konstfull-vase-verre-givre-vert__1030417_pe836273_s5.jpg?f=xxl'],
        # 'images':['https://www.ikea.com/fr/fr/images/products/konstfull-vase-verre-givre-vert__1030416_pe836271_s5.jpg?f=xxl', 'https://www.ikea.com/fr/fr/images/products/konstfull-vase-verre-givre-vert__1030417_pe836273_s5.jpg?f=xxl'],
         'price':44.75,
        'colours':5

    },
    {
        'id':104,
        'name':'Rattan Bed', 
        'type':'Bed',
        'material':'Rattan',
                'images':['data:image/png;base64,{}'.format(base64.b64encode(open('rattanBed.png', 'rb').read()).decode()),'https://www.ikea.com/gb/en/images/products/vevelstad-bed-frame-with-2-headboards-white-tolkning-rattan__1138249_pe879929_s5.jpg?f=xxl'],
        # 'images':['https://www.ikea.com/gb/en/images/products/vevelstad-bed-frame-with-2-headboards-white-tolkning-rattan__1113894_pe871584_s5.jpg?f=xxl','https://www.ikea.com/gb/en/images/products/vevelstad-bed-frame-with-2-headboards-white-tolkning-rattan__1138249_pe879929_s5.jpg?f=xxl'],
        'price':379.99,
        'colours':1

    },
    {
        'id':105,
        'name':'Wooden Thick Bed', 
        'type':'Bed',
        'material':'Wood',
        'images':['data:image/png;base64,{}'.format(base64.b64encode(open('whiteBed.png', 'rb').read()).decode()), 'https://www.ikea.com/gb/en/images/products/idanaes-bed-frame-with-storage-white-luroey__1101523_pe866702_s5.jpg?f=xl'],
        # 'images':['https://www.ikea.com/gb/en/images/products/idanaes-bed-frame-with-storage-white-luroey__1151017_pe884724_s5.jpg?f=xl', 'https://www.ikea.com/gb/en/images/products/idanaes-bed-frame-with-storage-white-luroey__1101523_pe866702_s5.jpg?f=xl'],
        'price':230.00,
        'colours':2

    },
       {
        'id':106,
        'name':'Black Wardrobe', 
        'type':'Wardrobe',
        'material':'Wood',
                'images':['data:image/png;base64,{}'.format(base64.b64encode(open('blackWardrobe.png', 'rb').read()).decode()), 'https://www.ikea.com/gb/en/images/products/rakkestad-wardrobe-with-3-doors-black-brown__0823988_pe776019_s5.jpg?f=xxl'],

        # 'images':['https://www.ikea.com/gb/en/images/products/rakkestad-wardrobe-with-3-doors-black-brown__0823987_pe776018_s5.jpg?f=xl', 'https://www.ikea.com/gb/en/images/products/rakkestad-wardrobe-with-3-doors-black-brown__0823988_pe776019_s5.jpg?f=xxl'],
        'price':160.15,
        'colours':1

    },
       {
        'id':107,
        'name':'Metal Sidetable', 
        'type':'Table',
        'material':'Metal',
                'images':['data:image/png;base64,{}'.format(base64.b64encode(open('sidetable.png', 'rb').read()).decode()), 'https://www.ikea.com/us/en/images/products/gladom-tray-table-black__1058801_ph163156_s5.jpg?f=xxl'],

        # 'images':['https://www.ikea.com/us/en/images/products/gladom-tray-table-black__0567223_pe664991_s5.jpg?f=xxl', 'https://www.ikea.com/us/en/images/products/gladom-tray-table-black__1058801_ph163156_s5.jpg?f=xxl'],
        'price':29.75,
        'colours':4

    },
    {
        'id':108,
        'name':'Glass Desk', 
        'type':'Desk',
        'material':'Glass',
        'images':['data:image/png;base64,{}'.format(base64.b64encode(open('whiteDesk.png', 'rb').read()).decode()), 'https://www.ikea.com/us/en/images/products/malm-dressing-table-white__1154625_pe886239_s5.jpg?f=xxl'],

        # 'images':['https://www.ikea.com/us/en/images/products/malm-dressing-table-white__0805994_pe769781_s5.jpg?f=xxl', 'https://www.ikea.com/us/en/images/products/malm-dressing-table-white__1154625_pe886239_s5.jpg?f=xxl'],
        'price':299.99,
        'colours':1

    },
    {
        'id':109,
        'name':'Wood Armchair', 
        'type':'Armchair',
        'material':'Wood',
        'images':['data:image/png;base64,{}'.format(base64.b64encode(open('armchair.png', 'rb').read()).decode()), 'https://www.ikea.com/us/en/images/products/ekenaeset-armchair-kilanda-light-beige__1179060_pe895831_s5.jpg?f=xxl'], 

        # 'images':['https://www.ikea.com/us/en/images/products/ekenaeset-armchair-kilanda-light-beige__1109687_pe870153_s5.jpg?f=xxll', 'https://www.ikea.com/us/en/images/products/ekenaeset-armchair-kilanda-light-beige__1179060_pe895831_s5.jpg?f=xxl'], 
        'price':420.85, 
        'colours':10

    }
]

@app.route('/')
def home():
    return jsonify('This is the home'), 200


# @app.route('/products', methods=['GET'])
# def getProducts():
#     return jsonify(products), 200

@app.route('/products', methods=['GET'])
def getProducts():
    try:
        products = get_products()
        list_of_products = []
        for item in products:
            list_of_products.append({
                'id':item[0],
                'name':item[1],
                'type':item[2],
                'material':item[3],
                'price':item[4],
                'colours':item[5],
                'image_url':item[6],
                'image_data':item[7]
            })
        return jsonify(list_of_products), 200
    except Exception as e:
        return jsonify({'error':str(e)}, 400)


if __name__ == '__main__':
    app.run()