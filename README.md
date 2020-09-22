# DataMade Code Challenge: Noah Marcus' Submission

This guide has been modified from the README provided by DataMade.

To get started, clone this repo and follow the instructions below.

## Installation

Development requires a local installation of [Docker](https://docs.docker.com/install/)
and [Docker Compose](https://docs.docker.com/compose/install/). These are the
only two system-level dependencies you should need.

Once you have Docker and Docker Compose installed, build the application containers:

```
docker-compose build
```

## Running the app 

Next, you can run the app with the following command:

```
docker-compose up
```

The app will log to the console, and you should be able to visit it at http://localhost:8000.

## Testing

You can run some tests using Docker:

```bash
docker-compose -f docker-compose.yml -f tests/docker-compose.yml run --rm app
```
