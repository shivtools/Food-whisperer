# Food whisperer - never miss out on your favorite food item ever again!

A tiny cronjob I set up on my Mac that uses a web scraper daily to fetch lunch and dinner menus from dhall. Sends me an email if my chosen food items are available at my university's dining hall.

Anyone who knows me knows that I am always hungry and I like to take shortcuts too when possible. I set up this cronjob to get dhall's lunch and dinner menu's from the university's website and to alert me by email whenever cream puffs or french silk pie is available. This way I will never miss out on having lunch/dinner the day that UR's dining hall is serving my favorite food items.

NOTE: To use this, you will need to have a sendgrid account. This doesn't work without one!

Run it by navigating to the proper directory and typing:

``` 
#set up the cron job to run everyday at 10am (on a linux system)
crontab -e
0 10 * * * path to this folder/scraper.py 

#alternatively just run the script as it is.
python scraper.py
```

Sendgrid's emails often go to Spam in gmail! Mark these emails 'Not spam' and hopefully they'll reach your inbox someday :) 

Please note that this project wasn't created with the intention to infringe upon any data privacy laws. It was only made to satiate my incurable and everlasting hunger.


