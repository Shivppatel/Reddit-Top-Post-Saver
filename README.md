# Reddit-Top-Post-Saver
This program takes will create a new folder in the posts directory of the subreddit supplied in the command line argument containing the top 25 posts and 25 comments from the sub in a txt file. 

Setup Requirements 
- 
  1) pip install praw
  2) get an api key from https://www.reddit.com/prefs/apps
  3) Open up Save_top_posts.py and fill in your key data for the variables CLIENT_ID, CLIENT_SECRET, and USER_AGENT

How to Run
 - 
  1) cd into the root of the folder
  2) python Save_top_posts.py askReddit(the subreddit you wich to save the top posts from)
  3) The program will save all the files in a folder the same name as the subreddit in the Posts folder.

How to Customize
  -
  1) Open file named Save_top_posts.py in the root directory
  2) You have the option to change the two variables named DEFAULT_NUM_POSTS and DEFAULT_NUM_COMMENTS which will change how     many posts and comments get save each time you run the progam.
