import os
import praw
import re
import pdb

reddit=praw.Reddit("bot1")  

if not os.path.isfile("file.txt"):
    already=[]
else:
    with open("file.txt",r) as f:
        already=f.read()
        already=already.split("/n")
        already=list(filter(None,already))

subreddit1 = reddit.subreddit('pythonforengineers')


for submission in subreddit1.hot(limit=10):
    print(submission.title)
    if submission.id not in already:
        if(re.search("I love Python",submission.title,re.IGNORECASE)):
                submission.reply("Me too man me too")
                print("replied to ",submission.id)
                already.append(submission.id)

with open("file.txt","w+") as f:
    for post_id in already:
        f.write(post_id+'\n')


