# Movie Embeddings Generator README

## Overview

The Movie Embeddings Generator is a Python-based application designed to enhance movie search functionality within a MongoDB database by utilizing semantic embeddings. By generating and utilizing embeddings from movie plot descriptions, the application allows for contextually rich, semantic searches that go beyond simple keyword matching. This approach leverages the Hugging Face API for embedding generation and MongoDB's powerful vector search features.

## Features

- Secure management of sensitive credentials using environment variables.
- Integration with MongoDB for data storage and retrieval.
- Use of the Hugging Face API to generate semantic embeddings for text.
- Implementation of MongoDB vector search to enable semantic search based on plot descriptions.

## Prerequisites

- MongoDB (local installation or access to an Atlas cluster)
- Python 3.6 or later
- An active Hugging Face account with an API token

## Setup Instructions

### Environment Preparation

1. Clone the repository and navigate into the project directory:

   ```sh
   git clone <repository-url>
   cd <project-directory>
