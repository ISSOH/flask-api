# cars_api

This is a simple example of Flask REST API. The main goal of project is build, test and deploy API on AWS via Elastic Beanstalk service.
Some concepts to design and implement a complex API REST are missing. please be bear with me 😃

## Examples
This is just an example of API in order to trigger gitlab ci pipeline. Below some  implemented endpoints in this API

| Method | URL       | Description             |
|--------|-----------|-------------------------|
| GET    | /cars      | Get all cars            |
| GET    | /cars/3 | Get a single car by its id |
| POST   | /cars      | Add car                 |

## Tools
 In oder to reach purpose of project, we have used some AWS services:
 - Elastic Beanstalk
 - S3
 - EC2
 - IAM

# Gitlab CI
The pipeline has 3 stages and 4 jobs:
+ smoke test: The smoke test as its name suggests is a simple test to check if our application properly works
+ unit test: To test somme implemented functions in application. To achieve we are using unittest library
+ build: To create a zip file as artifact to deploy
+ deploy: To deploy our application

Note: Like I told, a lot of things can be added in application like security and so on


