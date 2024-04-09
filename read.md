# Movie Embeddings Generator

This project focuses on enhancing the search capabilities of a MongoDB database containing movie information. By utilizing the power of large language models (LLMs) for generating embeddings of movie plots, we can perform semantic search operations. This allows us to find movies based on the meaning and context of their plots rather than relying solely on keyword matches. The project leverages the Hugging Face API for generating embeddings and MongoDB's vector search feature for querying.

## Features

- **Environment Variable Management**: Securely manage sensitive information such as database connection strings and API tokens using environment variables.
- **MongoDB Integration**: Connect to a MongoDB database, specifically to the `sample_mflix` database's `movies` collection, demonstrating practical usage of MongoDB with Python.
- **Semantic Embedding Generation**: Utilize the Hugging Face API to generate embeddings for movie plots, enabling advanced semantic search capabilities within the MongoDB collection.
- **Semantic Search in MongoDB**: Perform semantic searches on the movie collection to find movies based on the contextual meaning of their plots.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- MongoDB installed and running locally or access to a MongoDB Atlas cluster.
- Python 3.6+ installed on your machine.
- A Hugging Face account with an API token to use their services for generating embeddings.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <project-directory>
