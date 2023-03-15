# Portfolio-project - General over view
this project is a real estate web app with a unique functionalities which will bridge the gap between the property buyers and the sellers. To get rid of the long chain of property agent which mostly extort outrageously both the buyers and the sellers. Ensuring the authenticity of the properties, making sure they are linked to the legitimate owners. Providing a platform for the owners to market the properties they intend to sell wich aims at bringing about cost reduction of properties as no extra charges are linked to any of the properties sold on this website. This will in turn help property owners sell their properties faster without the traditional stress and unnecessary delay. What the portfolio project will not solve: Auntentified.ng is not liable to verifying the present and future weather condition effects or other physical conditions on properties sold on the website as the buyers must inspect the present condition of properties and investigate the future durability of the property before buying.

## Table of Content
* Environment
* File Descriptions
* Examples of use
* Bugs
* Authors
* License

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## base_model.py - The BaseModel class from which future classes will be derived

* def __init__(self, *args, **kwargs) - Initialization of the base model
* def __str__(self) - String representation of the BaseModel class
* def save(self) - Updates the attribute updated_at with the current datetime
* def to_dict(self) - returns a dictionary containing all keys/values of the instance
* def delete(self): - delete the current instance from the storage
* Classes inherited from Base Model:

* amenity.py
* city.py
* place.py
* review.py
* state.py
* user.py
## web_dynamic/ directory contains the dynamic version of portfolio-project:
/models/engine directory contains File Storage class that handles JASON serialization and deserialization :
file_storage.py - serializes instances to a JSON file & deserializes back to instances

def all(self) - returns the dictionary __objects
def new(self, obj) - sets in __objects the obj with key .id
def save(self) - serializes __objects to the JSON file (path: __file_path)
 def reload(self) - deserializes the JSON file to __objects
 
 ## Examples of use
 
 Portfolio-project

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit

## Bugs
No known bugs at this time.

## Authors
 * [Ikenna Ezeanyaeji](https://github.com/charlykso)
 * [Glory Chioma Anunah](https://github.com/glorycornel)
 * [Juliet Owanku](https://github.com/julietowah)
 
 
 ## License
Public Domain. No copy write protection.
 
 
 
 
 
 
 
 
 
 
 
 
