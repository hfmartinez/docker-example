# ML Model + Docker + FastAPI

## General description

This repository shows an example using FastAPI and Docker to run a simple machine learning model (Random Forest Classifier) ​​trained with the scikit-learn library.

## Quick start

There are two important scripts in this repository:

- generate-model.py: This file downloads the dataset ([mnist_784](https://towardsdatascience.com/784-dimensional-quantum-mnist-f0adcf1a938c)), trains the model (Random Forest Classifier) ​​and generates a new file with the already trained model.
- app.py: This file creates an endpoint to process HTTP requests to get a prediction using the pre-trained model

### Install dependencies

> **Note:** It is mandatory to have Python and Pip installed in your environment

To install the dependencies run the following command:

```
pip install -r requirements.txt
```

### Train the model

To train the model run the following command:

```
python generate-model.py
```

### Run the FastAPI application

To run the FastAPI application run the following command:

```
uvicorn app:app --reload
```

### Build and run the docker container

To build the docker container run the following command:

```
docker build -t hfmartinez/ml-fastapi .
```

To run the docker container use the following command:

```
docker run --name test -p 5500:5500 hfmartinez/ml-fastapi
```

## References

- [NeuralNine](https://www.youtube.com/watch?v=5PgqzVG9SCk&t=694s)
- [MNIST_784 Repository](https://towardsdatascience.com/784-dimensional-quantum-mnist-f0adcf1a938c)
