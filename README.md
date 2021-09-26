Implemented Twitter service :

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

below API's were consumes

1. Endpoint **/looktweet/<username> is created** - which cosumes twitter get tweets by userid 
and return the tweets back in response. 
This end point shows tweets on the html page .
Twitter API picked - https://api.twitter.com/2/tweets/:id where id is the **user id **
  Pick below username in place of username variable in the endpoint.
Elonmusk
Britneyspear
Katyperry
rihanna
taylorswift13
ArianaGrande
justinbieber
BrunoMars
ladygaga

 
  To Run the project add below lines
  export FLASK_ENV= developement
  export FLASK_APP=run.py
  flask run 
  
