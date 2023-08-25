# Instagramcollector
Instagram data collector RestAPI


# What is it?

it can get followers of an instagram username


## Installation

```
pipenv install --dev
```

After that install mongodb and run the mongod service

then edit .env file if needed

## Run

```
pipenv shell
uvicorn restapi.app:app --reload
```

## how use it ?

check http://127.0.0.1:8000/docs