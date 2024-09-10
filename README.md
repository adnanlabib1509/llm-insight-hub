# LLM Insight Hub

LLM Insight Hub is a full-stack application that provides a user-friendly interface for interacting with various Language Model (LLM) functionalities, including text generation, sentiment analysis, and named entity recognition. It also helps in gathering performance insights from these LLM models.

## Project Structure

```
llm-insight-hub/
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   ├── services/
│   │   │   └── ...
│   │   ├── assets/
│   │   └── environments/
│   ├── angular.json
│   ├── package.json
│   └── tsconfig.json
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── utils/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## Features

- **Text Generation**: Generate text using models like GPT-2, BERT, and T5.
- **Sentiment Analysis**: Analyze sentiment using models like BERT, RoBERTa, and DistilBERT.
- **Named Entity Recognition**: Perform NER using models like spaCy, Flair, and Stanford NER.
- **Performance Dashboard**: View and compare model performance metrics.
- **User Feedback**: Submit and view feedback on model performance.

## Prerequisites

- Node.js and npm (for Angular frontend)
- Python 3.9+ (for FastAPI backend)
- Docker and Docker Compose (for containerized backend)

## Setup and Installation

### Backend

1. Navigate to the backend directory:

```
cd backend
```

2. Build and start the Docker container:

```
docker-compose up --build
```

The backend API will be available at `http://localhost:8000`

### Frontend

1. Navigate to the frontend directory

```
cd frontend
```

2. Install dependencies:

```
npm install
```

3. Start the development server:

```
ng serve
```

The frontend application will be available at `http://localhost:4200`

## Usage

After starting both the backend and frontend servers:

1. Open a web browser and go to `http://localhost:4200`.
2. Use the navigation menu to access different features:

- Text Generation
- Sentiment Analysis
- NER Visualization
- Performance Dashboard
- User Feedback

## Deployment

For production deployment:

1. Build the Angular application:

```
cd frontend
ng build --prod
```

2. Update the `docker-compose.yml` file to include a web server for serving the built Angular files.

3. Configure environment variables for production settings

4. Use Docker Compose to builod and run both frontend and backend containers

## License

This project is licensed under the MIT License.