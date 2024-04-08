import pymongo
import requests
import os
from dotenv import load_dotenv

#load dotenv 
load_dotenv()


#load env files
mongo_client_url = os.getenv('MONGO_CLIENT_URL')
hf_token = os.getenv('HF_TOKEN')
embedding_url = os.getenv('EMBEDDING_URL')

client =  pymongo.MongoClient(mongo_client_url)
db = client.sample_mflix
collection = db.movies

#generate LLM embeddings for posgresdb
def generate_embeddings(text:str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Beare {hf_token}"},
        json={"inputs":text}
    )
    if response.status_code != 200:
        raise ValueError(f"Request failed with status code{response.status_code}:{response.text}")
    return response.json 