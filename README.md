# RAG Chatbot

This project is a conversational chatbot using **Retrieval-Augmented Generation (RAG)**, designed to provide accurate responses by retrieving relevant information from a knowledge base and combining it with generative AI. The chatbot utilizes various technologies for classification, data storage, sensitive data masking, and deployment.

## Features

- **RAG Model**: The chatbot uses Retrieval-Augmented Generation (RAG) to enhance response accuracy by pulling information from external sources.
- **Classification ML Model**: Integrated with a machine learning classification model trained and deployed using **Google Cloud AutoML**.
- **Vector Database**: Pinecone is used as the vector database (vectorDB) for efficient storage and retrieval of document embeddings.
- **Automated Data Pipeline**: An **Airflow pipeline** automatically updates and embeds new documents in Pinecone when uploaded to a Google Cloud Storage (GCS) bucket.
- **Sensitive Data Masking**: Integrated **Microsoft Presidio** for detecting and masking personally identifiable information (PII) and other sensitive data before storing or processing.
- **Dockerized Deployment**: The entire solution is containerized using **Docker** for easy deployment and scaling.

## Project Architecture

1. **Data Flow**:
    - New documents are uploaded to a GCS bucket.
    - An Airflow pipeline monitors the GCS bucket for new documents.
    - Documents are processed, verified, and embedded into the vector database (Pinecone) for future retrieval.

2. **Chatbot Functionality**:
    - The RAG model retrieves relevant document embeddings from Pinecone.
    - Combined with generative AI, it provides accurate and contextually relevant responses.
    - The chatbot also leverages a GCP AutoML classification model to assist with content categorization during the interaction.

3. **Data Masking**:
    - Sensitive data within the documents and user interactions is detected and masked using Microsoft Presidio before the data is sent for embedding or storage.

## Components

- **RAG Chatbot**: Utilizes document retrieval from Pinecone to augment generative AI responses.
- **Classification Model**: Deployed on GCP AutoML for content classification tasks.
- **Pinecone VectorDB**: Stores document embeddings for fast retrieval during conversations.
- **Airflow**: Automates the ingestion and embedding of documents into Pinecone.
- **Microsoft Presidio**: Masks sensitive information, such as PII, before processing.
- **Docker**: Facilitates easy deployment and scaling via containerization.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your system.
- GCP project set up with AutoML and Google Cloud Storage (GCS) access.
- Pinecone account with a created index for storing embeddings.
- Microsoft Presidio installed for sensitive data masking.

### Steps

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd rag-chatbot
    ```

2. **Set up Docker**:
    - Build the Docker container:
      ```bash
      docker-compose up --build
      ```

    - The container will automatically run the Airflow instance and deploy the chatbot.

3. **Configure Google Cloud and Pinecone**:
    - Set up your GCS bucket to upload documents.
    - Configure your Pinecone index with the appropriate settings.
    - Ensure you have Google Cloud credentials available for accessing GCP AutoML and GCS.

4. **Add Environment Variables**:
    - Set up the environment variables for accessing GCP, Pinecone, and Presidio. These should include:
      - `GCP_PROJECT_ID`
      - `PINECONE_API_KEY`
      - `PRESIDIO_API_ENDPOINT`

5. **Run the Airflow Pipeline**:
    - Airflow will automatically monitor the GCS bucket for new document uploads and update Pinecone accordingly.
    - Trigger DAGs manually via the Airflow UI (`http://localhost:8080`) or let the sensor detect changes automatically.

6. **Start the Chatbot**:
    - Once everything is up and running, the chatbot is available via a REST API or as a web interface (if configured).
    - The chatbot will retrieve relevant documents from Pinecone and classify responses using the GCP AutoML classification model.

## Key Technologies

- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval and generative AI for intelligent chatbot responses.
- **Google Cloud AutoML**: Trains and deploys the classification model.
- **Pinecone**: Vector database for storing and retrieving document embeddings.
- **Microsoft Presidio**: Detects and masks sensitive information (PII) in documents and conversations.
- **Airflow**: Automates the document ingestion pipeline from GCS to Pinecone.
- **Docker**: Containerizes the entire system for consistent deployment.

## Updates

### Version 2.0:

- **New Document Pipeline**: Added a separate Airflow pipeline that automatically updates new documents uploaded to the GCS bucket. The pipeline verifies the documents, generates embeddings, and updates Pinecone. Check the [chatbot_dag](https://github.com/oliveberch/chatbot_dag) project here.
- **Sensitive Data Masking**: Microsoft Presidio integrated to detect and mask sensitive data such as personally identifiable information (PII) before processing the documents.
- **Enhanced Classification**: GCP AutoML classification model fine-tuned for better accuracy and response categorization.

## Usage

- **RAG Chatbot**: Interact with the chatbot via API or web UI for conversational responses.
- **Document Upload**: Upload new documents to the GCS bucket. Airflow will automatically process and update the vector database.
- **Masked Data**: All sensitive data within uploaded documents is masked before being processed and stored.

## Future Enhancements

- Integration with more advanced generative AI models.
- Expansion of sensitive data detection beyond PII.
- Improved document verification and processing workflows.
