## Inspiration
COVID-19 showed us how vulnerable we can be when traveling and how dangerous many nations are, either due to public health crises or political instability. So we thought it would be important that when traveling goes back to a new normal, that we can prepare and check any dangers in our country.

## What it does
Travel Assess takes in the user's current nation they reside and the country they wish to travel. Then, the program searches through the web, search any top and relevant news, along with any news on the relationship of the two countries. From their, the program reads through the contents of the news it gathers to determine the overall sentiment of that nation, Too many negative or dangerous connotation words will trigger a "Danger" response, and vice versa. The program then reports to the user how safe their destination currently is, along with the top headlines. 

## How I built it
The program is built in python, with the user interface being built with the streamlit API. The natural language processing is determined by the nltk and the vaderSentiment API's. The newsapi-python API gathers the news articles based off three different categories: top headlines of the destinations, all relevant news on destination, and all top headlines relating to the source and destination country relations. 

## Challenges I ran into
A few challenges we ran into include the webscrapping with newsapi-python as it limits how many requests can be pulled each day. Learning the nltk API also had some issues, as it was difficult to pull the contents from the news in a multidimensional array and to find its overall sentiment. 
Other issues included getting headlines to appear in streamlit, images of articles not showing up, and creating an algorithm that determines the sentiment of the news to determine how safe it was to travel.

## Accomplishments that I'm proud of
I'm most proud of the ease of use a user has with the program. All they have to do is input their country and destination and the program does all the heavy work for them, giving them information they could take hours on their own.

## What I learned
We learned how useful and powerful APIs work and ways to utilize them in very applicable and unique ways. Learning the nltk and newsapi-python APIs are extraordinarily useful for gathering and analyzing string type data. 

## What's next for Trip Assess
Future features of Trip Assess we hope to see is creating user profiles, trip cost calculator, and ways to share with travel agencies to implement in their own businesses.
