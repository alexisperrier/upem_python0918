# Reddit

* create account
* create app

D0jQQnHZ3BhRDA
DU9ZifID860X_avJSogFpWmpM6E

https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

https://praw.readthedocs.io/en/latest/getting_started/quick_start.html


user_agent = "osx:upemdemo:v.0.0.1 (by /u/alexperrier)"

import praw

reddit = praw.Reddit(client_id='D0jQQnHZ3BhRDA',
                     client_secret='DU9ZifID860X_avJSogFpWmpM6E',
                     user_agent=user_agent)

reddit.read_only

subreddit = reddit.subreddit('montreal')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of ...

for submission in subreddit.hot(limit=10):
    print()
    print("="*30)
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
    all_comments = submission.comments.list()
    print("="*10 + " {}  comments   ".format(len(all_comments)))
    for c in all_comments[:min(10, len(all_comments))]:
        print("- {}".format(c.body))


* sleep
* aggreger les textes dans une df
* en fonction de la langue

* quels sont les themes ?
* autres champs
