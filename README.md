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

**Note:** You can use the following address strings:

- ✅ Valid: `123 main st chicago il`
- ❌ Invalid: `123 main st chicago il 123 main st`

## Testing

You can run some unit tests using Docker:

```bash
docker-compose -f docker-compose.yml -f tests/docker-compose.yml run --rm app
```

There are two unit tests that make requests to the API endpoint `address-parse` and verify that it passes or fails. 

The first test checks for a successful run with the test string `123 main st chicago il`. We expect a success return code of 200, and some return data (the input string, an ordered dictionary of parsed address information, and the address type).

The second test uses a known invalid string (`123 main st chicago il 123 main st`) to ensure the proper error is returned. We expect a return code of 400 and the error response's detail to be 'RepeatedLabelError'.