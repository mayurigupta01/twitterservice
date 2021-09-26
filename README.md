Implemented Twitter service :

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

**To Run the project -follow below steps :**

git clone https://github.com/mayurigupta01/twitterservice.git

cd twitterservice

**./serverStart.sh**

 To run the unit test

**python3 test.py**

Now follow below endpoints :

**API End points**
1. homepage : http://127.0.0.1:5000/ 

2. **Tweets LookUp by username** :Get http://127.0.0.1:5000/looktweet?username=<>
Choose username from the  list and enter in webpage under 
   Elonmusk,
   Britneyspear,
   Katyperry,
   rihanna,
   taylorswift13,
   ArianaGrande,
   justinbieber,
   BrunoMars,****
   ladygaga

Home Page allowing the user to enter the twitter user you wish to retrieve tweets. 
![](../../../../var/folders/x9/w64smj897mj2jpyfw2f_p84c0000gn/T/TemporaryItems/NSIRD_screencaptureui_QtcMcp/Screen Shot 2021-09-26 at 11.00.02 AM.png)


![](../../../../var/folders/x9/w64smj897mj2jpyfw2f_p84c0000gn/T/TemporaryItems/NSIRD_screencaptureui_9fNb2J/Screen Shot 2021-09-26 at 11.03.17 AM.png)

 Click on Submit button and user can view tweets of the User entered from the webpage.
API Call - http://127.0.0.1:5000/looktweet?username=Katyperry

![](../../../../var/folders/x9/w64smj897mj2jpyfw2f_p84c0000gn/T/TemporaryItems/NSIRD_screencaptureui_D10Zjb/Screen Shot 2021-09-26 at 11.05.04 AM.png)


2. Delete Tweet 



3. Search recent tweet 


4. Update Tweet 