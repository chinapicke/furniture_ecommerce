DROP DATABASE IF EXISTS Shop_Management;
CREATE DATABASE Shop_Management;
USE Shop_Management;

CREATE TABLE Products(
Product_ID INT AUTO_INCREMENT PRIMARY KEY,
Product_Name VARCHAR(50), 
Product_Type VARCHAR(50),
Material VARCHAR(50),
Image_Link VARCHAR(240), 
Price DECIMAL(5,2), 
Colours INT
);

CREATE TABLE Image_Table (
    Image_ID INT PRIMARY KEY AUTO_INCREMENT,
    Product_ID INT,
    Image_Data LONGBLOB, 
FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

ALTER TABLE Image_Table AUTO_INCREMENT=1;
ALTER TABLE Products AUTO_INCREMENT=101;

INSERT INTO Products (Product_Name, Product_Type, Material, Image_Link, Price, Colours) VALUES
('Basic Sofa', 'Sofa', 'Fabric', 'https://www.ikea.com/us/en/images/products/linanaes-loveseat-vissle-beige__0985924_pe816903_s5.jpg?f=xl', 524.79, 6),
('Glass Lamp', 'Lamp', 'Glass', 'https://www.ikea.com/us/en/images/products/pilblixt-table-lamp-white-light-green-glass-gold-effect-metal__1132171_pe878166_s5.jpg?f=xl', 99.75, 2),
('Glass Vase', 'Home_Decor', 'Glass', 'https://www.ikea.com/fr/fr/images/products/konstfull-vase-verre-givre-vert__1030417_pe836273_s5.jpg?f=xxl', 44.75, 5),
('Rattan Bed', 'Bed', 'Rattan', 'https://www.ikea.com/gb/en/images/products/vevelstad-bed-frame-with-2-headboards-white-tolkning-rattan__1138249_pe879929_s5.jpg?f=xxl', 379.99, 1),
('Wooden Thick Bed', 'Bed', 'Wood', 'https://www.ikea.com/gb/en/images/products/idanaes-bed-frame-with-storage-white-luroey__1101523_pe866702_s5.jpg?f=xl', 230.00, 2),
('Black Wardrobe', 'Wardrobe', 'Wood', 'https://www.ikea.com/gb/en/images/products/rakkestad-wardrobe-with-3-doors-black-brown__0823988_pe776019_s5.jpg?f=xxl', 160.15, 1),
('Metal Sidetable', 'Table', 'Metal', 'https://www.ikea.com/us/en/images/products/gladom-tray-table-black__1058801_ph163156_s5.jpg?f=xxl', 29.75, 4),
('Glass Desk', 'Desk', 'Glass', 'https://www.ikea.com/us/en/images/products/malm-dressing-table-white__1154625_pe886239_s5.jpg?f=xxl', 299.99, 1),
('Wooden Armchair', 'Armchair', 'Wood', 'https://www.ikea.com/us/en/images/products/ekenaeset-armchair-kilanda-light-beige__1179060_pe895831_s5.jpg?f=xxl', 420.85, 10);

