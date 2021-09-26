Twitter Service Implementation

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

**How To Run the Project**

1) git clone https://github.com/mayurigupta01/twitterservice.git
2) cd twitterservice
3) ./serverStart.sh

**How To Run Unit Tests**

1) python3 test.py

Overview of **API Endpoints** Created in the Project

1) Homepage: http://127.0.0.1:5000/

2) **Tweets LookUp by Username**: Get http://127.0.0.1:5000/looktweet?username=<>
    * Allows the user to enter a twitter user they wish to retrieve tweets from

Choose username from the list and enter in webpage under Elonmusk, Britneyspear, Katyperry, rihanna, taylorswift13,
ArianaGrande, justinbieber, BrunoMars,****
ladygaga

Home Page allowing the user to enter the twitter user you wish to retrieve tweets.
![](../../../../var/folders/x9/w64smj897mj2jpyfw2f_p84c0000gn/T/TemporaryItems/NSIRD_screencaptureui_QtcMcp/Screen Shot 2021-09-26 at 11.00.02 AM.png)

![](../../../../var/folders/x9/w64smj897mj2jpyfw2f_p84c0000gn/T/TemporaryItems/NSIRD_screencaptureui_9fNb2J/Screen Shot 2021-09-26 at 11.03.17 AM.png)

Click on Submit button and user can view tweets of the User entered from the webpage. API Call
- http://127.0.0.1:5000/looktweet?username=Katyperry

![](../../../../var/folders/x9/w64smj897mj2jpyfw2f_p84c0000gn/T/TemporaryItems/NSIRD_screencaptureui_D10Zjb/Screen Shot 2021-09-26 at 11.05.04 AM.png)

3) Search Most Recent Tweet
    * Allows the user to enter any query they wish and the most recent tweet from the user's query will be returned

4) Delete Tweet

5) Update Tweet 
