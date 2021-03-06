# Twitter Service Implementation

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

Authors: Aman Shah, Martin Duong, Mayuri Gupta, Pratiksha Shukla

Team: Squirtle Squad

## How to Run the Project

1. git clone https://github.com/mayurigupta01/twitterservice.git
2. cd twitterservice
3. ./serverStart.sh

## How to run Unit Tests

1. python3 test.py

## Overview of API Endpoints Created in the Project

- Homepage: http://127.0.0.1:5000/
  ![Capture13](https://user-images.githubusercontent.com/2999334/134846671-9120d5ff-2c7c-40f5-ba80-e3f2338d57ac.PNG)

- Tweet LookUp by Username: Get http://127.0.0.1:5000/looktweet?username=<>
  - Allows the user to enter a Twitter user they wish to retrieve tweets from.
  
    ![Capture3](https://user-images.githubusercontent.com/2999334/134836637-c171141a-0347-4c88-8f1f-cd1f02f66d7d.PNG)
    
  - Enter any username in the input text box and click Submit.
  
    ![Capture4](https://user-images.githubusercontent.com/2999334/134836731-4c7aaa90-63bf-4e1e-bc12-f8d59d84d256.PNG)
    
  - User is directed to API Route - http://127.0.0.1:5000/looktweet?username=ArianaGrande and the web page shows the retrieved tweets of the username entered.
  
    ![Capture5](https://user-images.githubusercontent.com/2999334/134836808-33185305-8956-40fb-a081-3fc90f434f9e.PNG)

- Search Most Recent Tweet
  - Allows the user to enter any query they wish and the most recent tweet from the user's query will be returned.
  - Returns a single, most recent tweet that contains the user's query, excluding Retweets.
  
    ![Capture](https://user-images.githubusercontent.com/2999334/134836424-17abf3a4-256a-4c39-8a18-8793a9598235.PNG)
    
    ![Capture6](https://user-images.githubusercontent.com/2999334/134837215-16e4b336-b963-4d8b-a0a5-928fe6b1cc5f.PNG)
    
    ![Capture9](https://user-images.githubusercontent.com/2999334/134838053-1b3d37be-0cb0-456f-8c8e-2572925ba631.PNG)
    
  - Tweets that have no results will return “No Tweets Found”
  
    ![Capture11](https://user-images.githubusercontent.com/2999334/134847007-e76f88a6-ef20-4335-9270-00302f18f737.PNG)


- Get the Followers of a Given Username
  - Allows the user to enter any Twitter user they wish and a list of their Followers will be returned.
  
    ![Capture2](https://user-images.githubusercontent.com/2999334/134836572-b53ad124-8e31-4ef4-bf21-1efc93363729.PNG)
    
    ![Capture7](https://user-images.githubusercontent.com/2999334/134837365-b31be878-b394-4788-be04-475b96c82749.PNG)
    
    ![Capture8](https://user-images.githubusercontent.com/2999334/134838033-5d206fe6-96a4-4f72-acd0-407afcf5fe2c.PNG)

- Update Tweet 

- Post Tweet
  - Allows the user to post a tweet
  
![Capture12](https://user-images.githubusercontent.com/2999334/134846899-08892dda-2ec3-46c7-8f39-8ad806c85b89.PNG)

![Capture15](https://user-images.githubusercontent.com/2999334/134846906-8b4d813c-e2e5-4138-af71-d797c2316679.PNG)

![Capture16](https://user-images.githubusercontent.com/2999334/134846913-3b2dc0a5-f044-4bc4-8c37-0eb08a3b8ec1.PNG)

## Unit Tests
- Unit Tests for the following functions: Tweet LookUp by Username, Search Most Recent Tweet, and Get the Followers of a Given Username

  ![Capture14](https://user-images.githubusercontent.com/2999334/134846783-21e7d565-d5d2-44cb-ad84-09bc736ef1c9.PNG)
