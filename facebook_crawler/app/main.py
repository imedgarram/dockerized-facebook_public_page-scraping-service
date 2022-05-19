import fastapi
from fastapi import FastAPI
import uvicorn
import pymongo
from bson.objectid import ObjectId
import requests
import scraper
from scraper import scraping



#Database connection
try:
    client=pymongo.MongoClient("mongodb://root:example@mongo:27017/")
    db=client["Reuters"] # mongodb Database
    mycol=db["headers"] # collection inside Reuters database
    client.server_info()  # trigger exception if cannot connect to db
except:
    print("ERROR --- Cannot connect to db ")

app = FastAPI()


@app.post("/reuters")
def scrap_and_save():
    scraped_data=scraping()
    for elem in scraped_data:
        mycol.insert_one(elem)
    return  {"message":"data was scraped successfully from Reuters----see saved data at http://localhost:8081/"}


if __name__ =='__main__':
     uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")





