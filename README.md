# Twitter Service Implementation

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

Authors: Aman Shah, Martin Duong, Mayuri Gupta, Pratiksha Shukla

## How to Run the Project

1. git clone https://github.com/mayurigupta01/twitterservice.git
2. cd twitterservice
3. ./serverStart.sh

## How to run Unit Tests

1. python3 test.py

## Overview of API Endpoints Created in the Project

- Homepage: http://127.0.0.1:5000/

- Tweet LookUp by Username: Get http://127.0.0.1:5000/looktweet?username=<>
  - Allows the user to enter a twitter user they wish to retrieve tweets from.
    - [insert img here]
  - Enter any username in the above input text Box and click Submit.
    - [insert img here]
  - User is directed to API Route - http://127.0.0.1:5000/looktweet?username=ArianaGrande and the web page shows the retrieved tweets of the username entered.
    - [insert img here]

- Search Most Recent Tweet
  - Allows the user to enter any query they wish and the most recent tweet from the user's query will be returned.
    - [insert img here]

- Get the Followers of a given Username

- Update Tweet 

## Unit Tests
 - [insert img here]
