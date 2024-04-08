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
def generate_embedding(text: str) -> list[float]:

  response = requests.post(
    embedding_url,
    headers={"Authorization": f"Bearer {hf_token}"},
    json={"inputs": text})

  if response.status_code != 200:
    raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

  return response.json()

# for doc in collection.find({'plot':{"$exists":True}}).limit(50):
#   plot_data = {"source_sentence": doc['plot']}  # Keep the dictionary format
#   doc['plot_embedding_hf'] = generate_embedding(plot_data)
#   collection.replace_one({'_id': doc['_id']}, doc)


query = "imaginary characters from outer space at war"

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding_hf",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')