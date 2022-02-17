# Tariff Price API 
Energy price api which calculate unit price based on location.(Coding Challenge).

# Tech Stack 
- Python v3.10
- FastAPI (Latest) 
- NumPy

# Why I choose Fast API instead of Flask or django ?
-  Very high performance, on par with NodeJS and Go
-  Fast API validates the developer’s data type even in deeply nested JSON requests. 
-  Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.
-  Designed to be easy to use and learn. Less time reading docs 😃


## Test it online
[Here is the link](http://46.101.98.0:8002/docs#/default/post_data_main_get) If don’t want to setup the project locally and just wants to test it on your browser.

It’s running on the smallest digital ocean droplet 1 GB Memory / 25 GB Disk inside a docker container.

## Run Locally
I tired to make life easier for fellow developer to run the project locally without fiddling with Python versions and dependencies. Only prerequisite is Docker & docker-compose and some ☕.

1) Clone the project

```
git clone https://github.com/umerkhan95/tariff-price-api.git
```

2) Go to the project directory

```
cd tariff-price-api
```

3) Install dependencies

```
docker-compose up -d --build
```

*Build process could take few minutes,  Building wheel for numpy can take bit longer, its known issue in python community which needs a fix*

4) Tryout the API in OpenAPI (Swagger)

[http://localhost:8002/docs](http://localhost:8002/docs#/default/post_data_main_get)

## Expected Behaviour 
Submit address and energy usage data directly in OpenAPI Client

<img width="500" alt="post-data" src="https://user-images.githubusercontent.com/96595386/154400663-060f6435-0ce4-4f08-9a20-0dfee0db4d18.png">

Get the calculated result as response

<img width="500" alt="response-data" src="https://user-images.githubusercontent.com/96595386/154401014-85b352de-97fb-4b0d-afaa-c977b48dc560.png">

You can also use Postman or Good old Curl to get the same results:

## Test Server

**CURL Request** (Paste it in Terminal)

```
curl -X 'GET' \
  'http://46.101.98.0:8002/main?postal_code=10555&city=Nellischeid&street=Torstra%C3%9Fe&house_number=20&ykc=1000' \
  -H 'accept: application/json'
```

**Request URL**

```
http://46.101.98.0:8002/main?postal_code=10555&city=Nellischeid&street=Torstra%C3%9Fe&house_number=20&ykc=1000
```

## Local

**CURL Request** (Paste it in Terminal)

```
curl -X 'GET' \
  'http://localhost:8002/main?postal_code=10555&city=Nellischeid&street=Torstra%C3%9Fe&house_number=20&ykc=1000' \
  -H 'accept: application/json'
```

**Request URL**

```
http://localhost:8002/main?postal_code=10555&city=Nellischeid&street=Torstra%C3%9Fe&house_number=20&ykc=1000
```

## Improvements / ToDo’s

Due some time constrains I could only spend around 5-6 hours on the challenge this week, its was fun experience to test out  FastAPI for the first time. 


1) Currently reading data from CSV, response time will be much better if I use data persistence (Postgres or mariaDB).

2) Write some unit test to cross check the math and some integration tests with mock data to test api functionality and run them before the build process with Github Actions.

3) Restructure the project:


::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.

