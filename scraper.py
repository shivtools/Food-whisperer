#!/usr/bin/env python
#Author: Shiv Toolsidass, food enthusiast till the end of time.

import sendgrid

from bs4 import BeautifulSoup
from urllib2 import urlopen

sg = sendgrid.SendGridClient("<Your sendgrid username>", "<Your sendgrid password>") #use your own username and password yo! This won't work until you do.
message = sendgrid.Mail()

def make_soup(url):
    html = urlopen(url).read()
    # print html
    soup = BeautifulSoup(html, "lxml")
    span = [span.string for span in soup.findAll("span", "title")]
    for item in span:
        print item
        #list your favorite food items below
        if item.lower() == "cream puffs" or item.lower() == "french silk pie":
			sendemail(item); #call sendemail if either of these food items is found
			print "IMPORTANT! Your item: " + item + "is available. Don't miss out!" #print to console.

def sendemail(foodItem):
	message.add_to("shivtoolsidass@gmail.com") # email you want the email sent to
	message.set_from("The food whisperer <foodwhisperer@sendgrid.com>") #email you want it coming from 
	message.set_subject("Dhall has " + foodItem + " today! Drop whatever you are doing and go get some!") 
	message.set_html("You heard me!")

	sg.send(message) #send message using sendgrid
	print "sent email"

soup = make_soup("http://dining.richmond.edu/locations/heilman/index.html") # where url is the url we're passing into the original function
sendemail("creampuffs")