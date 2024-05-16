NLPower

## Overview
NLPower is a FastAPI-based service designed to provide real-time text analysis. It leverages some Natural Language Processing (NLP) libraries to offer functionalities such as sentiment analysis, keyword extraction, and text summarization.

This API can be used as a standalone service or integrated into front-end applications, data analytics tools, or any system that requires automated text understanding.

## Features
- **Sentiment Analysis**: Determine if the sentiment of the input text is positive or negative.
- **Keyword Extraction**: Extract significant keywords from the provided text.
- **Text Summarization**: Generate a concise summary of the given text.

## Technologies
- FastAPI
- spacy
- nltk

## Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed on your machine. It is also recommended to use a virtual environment for Python projects.

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/nlpower.git
   cd nlpower
   ```

2. Install required Python packages
    ```bash
   pip3 install -r requirements.txt
    ```

3. Download necessary NLP models
   ```bash
   python3 -m spacy download en_core_web_sm
   python3 -m nltk.downloader popular
   ```
   
### Running the API
1. Start the FastAPI server
   ```bash
   uvicorn app.main:app --reload
   ```
The API should now be running on `http://localhost:8000`. You can access the documentation at `http://localhost:8000/docs`.

## Usage
Here's an example of how to use the API via `curl`:

-  Sentiment Analysis
```bash
curl -X 'POST' \
  'http://localhost:8000/analyze/sentiment' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I love using FastAPI!"}'
```
   **Response**
   ```json
   {
     "sentiment": "Positive"
   }
   ```

- Keyword Extraction
```bash
curl -X 'POST' \
  'http://localhost:8000/analyze/keywords' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "FastAPI is a modern, fast (high-performance), web framework for building APIs."}'
```
   **Response**
   ```json
   {
     "result": "FastAPI, modern, fast, web, framework, APIs"
   }
   ```

- Text Summarization
```bash
curl -X 'POST' \
  'http://localhost:8000/analyze/summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "FastAPI is a great tool. It helps you build APIs really fast."}'
```
    **Response**
```json
    {
      "result": "FastAPI is a great tool."
    }
```

## Contribution
Contributions are welcome and appreciated. You can contribute in various ways such as submitting issues in our repo and creating pull requests for improvements to documentation or code.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/pedcapa/nlpower/blob/main/LICENSE) file for details.