# Instagramcollector
Instagram data collector RestAPI


# What is it?

it can get followers of an instagram username


## Installation

```
pipenv install --dev
```

After that install mongodb and run the mongod service

you should change default secret in .env file by generating the new one using this command :

```
openssl rand -hex 32
```

## Run

```
pipenv shell
uvicorn restapi.app:app --reload
```

## how use it ?

check http://127.0.0.1:8000/docs