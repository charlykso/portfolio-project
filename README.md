# Portfolio-project - General overview

this project is a real estate web app with a unique functionalities which will bridge the gap between the property buyers and the sellers. To get rid of the long chain of property agent which mostly extort outrageously both the buyers and the sellers. Ensuring the authenticity of the properties, making sure they are linked to the legitimate owners. Providing a platform for the owners to market the properties they intend to sell wich aims at bringing about cost reduction of properties as no extra charges are linked to any of the properties sold on this website. This will in turn help property owners sell their properties faster without the traditional stress and unnecessary delay. What the portfolio project will not solve: Auntentified.ng is not liable to verifying the present and future weather condition effects or other physical conditions on properties sold on the website as the buyers must inspect the present condition of properties and investigate the future durability of the property before buying.

## Table of Content

* Environment
* Models
* Description
* Web_dynamic
* Bugs
* Authors
* License

## Environment

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Models/directory contains classes used for this project:

[base_model.py](https://github.com/charlykso/portfolio-project/blob/master/models/base_model.py) - The BaseModel class from which future classes will be derived

* def __init__(self, *args, **kwargs) - Initialization of the base model
* def __str__(self) - String representation of the BaseModel class
* def save(self) - Updates the attribute updated_at with the current datetime
* def to_dict(self) - returns a dictionary containing all keys/values of the instance
* def delete(self): - delete the current instance from the storage

Classes inherited from Base Model:

* [address.py](https://github.com/charlykso/portfolio-project/blob/master/models/address.py)
* [property.py](https://github.com/charlykso/portfolio-project/blob/master/models/property.py)
* [user.py](https://github.com/charlykso/portfolio-project/blob/master/models/user.py)
* [review.py](https://github.com/charlykso/portfolio-project/blob/master/models/review.py)
* [property_img.py]((https://github.com/charlykso/portfolio-project/blob/master/models/property_img.py))
* [db_storage.py](https://github.com/charlykso/portfolio-project/blob/master/models/engine/db_storage.py)

## Description
This project is aimed at solving primarily the fundamental problem that plagues real estate sector which is fraud and unauthenticity of property beign sold to unassuming buyers at the dentriment of loosing their money. So, this project in operation with the state real estate database, will query every detail of properties being put up on the website (Authentified.ng) to be sold, and if the property details are not in sync with the property details on the state real estate database or the property details can't be found on the state real estate database it will dissalow its listing on the website thereby ensuring that only authentic properties are being listed and sold on authentified.ng.

## web_dynamic/ directory contains the dynamic version of portfolio-project:

## Bugs

No known bugs at this time.

## Authors

 * [Ikenna Ezeanyaeji](https://github.com/charlykso)
 * [Glory Chioma Anunah](https://github.com/glorycornel)
 * [Juliet Owanku](https://github.com/julietowah)
 
 
 ## License

Public Domain. No copy write protection.
 
 
 
 
 
 
 
 
 
 
 
 
