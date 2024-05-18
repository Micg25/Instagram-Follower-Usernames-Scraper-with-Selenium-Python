# Instagram-Follower-s-Usernames-Scraper-with-Selenium
This bot is made with Selenium, in order to make it work you have to manually add the values of your own cookies, you can easily take them by logging in instagram using your own browser and then opening the inspector element; once you opened it you have to go in the memory window and look for "cookie", once there you will see all of the cookies that instagram use to log you in. In my code you are gonna find the set of cookie you have to add but you'll have to modify the values of them with your own valid cookies values. By the way in the code you are gonna find comments where I tell you where you have to add some values.
Once you properly loaded your cookies (wich they have a long expire date so don't worry about updating them  frequently), you will have to change the "Profile_link" variable with the link of the profile you want to scrape from.
And you did it, once you'll start the code this will start fetching usernames from that profile, and once finished it is gonna save the usernames in a "usernames.txt" file.


Packages needed: pip install selenium

PS. Make sure to put your driver.exe in the same path of the code, or else to specify the path of the driver, or the selenium webdriver is not gonna work.
