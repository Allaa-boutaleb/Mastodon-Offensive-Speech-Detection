# PROJET-REDS

Lien d'edition du rapport : https://www.overleaf.com/3744136145fsrgwsmmzntf


## Based on this project

> [Docker Pipeline](https://github.com/molemae/docker_pipeline/)

Edited for specific use case of storing tweets in MongoDB.

## What we are doing
The task we want to do is to: Precisely classify a mastodon public toot as containing hate speech or not.

This project performs the following operations:
- Extract toots from the mastodon public server (number defined by the user, extracts the most recent toots.).
- Apply transformations to the extracted toots, and performs a labeling step which consists on adding lablels (1 for hate speech / 0 for non hate speech) using a pretrained model trained on this particular task (roberta from facebook model).
- Consider the obtained labeled dataset as our knowledge base (with labels being the ground truth), and then train our own model on this dataset with an experimental protocol, using many models.
- Select the best model, analyse the results and decide whether to trust our new model or not, discuss about everything we have.
- Implement a robust and clean code, using docker to simplify the portability of the Project as a whole (can be built on any os), and to support the production of our project (in a cloud environment).

## Run this project on your own machine

To run this project on your own machine, you need to perform the following steps:
- Make sure you have docker installed locally.
- Run the following commands on your terminal : 
    ```
    docker compose build
    ```
    This will build or rebuild images in the docker-compose. yml file
- Then start and attaches to containers for our needed services:
    ```
    docker compose up
    ```
- Once you have finished running the project, you can stop containers and remove containers, networks, volumes, and images created by up :
    ```
    docker compose down
    ```

## TODO
- [x] Define a use-case: it's not very clear how we expect the user to use this program
- [x] Define the criteria to fetch data, the number of toots we want
- [x] Select the model to be used (baseline/pretrained) to label our data and add the labeling code in main.py (now facebook roberta).
- [x] Select the model to be used to train our labeled dataset (classification task), and the metrics (imbalanced data) (now logistic regression, random forests, svm, decision trees).
- [x] Detail the ReadMe File (How to run the code as a whole) and add some guidelines for the report team
- [ ] Add a part for generating/analyzing plots and graphics and commenting the results