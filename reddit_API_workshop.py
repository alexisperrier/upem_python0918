# Reddit

* create account

# create app

https://www.reddit.com/prefs/apps



see also
https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

https://praw.readthedocs.io/en/latest/getting_started/quick_start.html



import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent=user_agent)

reddit.read_only

subreddit = reddit.subreddit('montreal')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of ...

k = 0
for submission in subreddit.new(limit=100):
    print(k, submission.score, submission.title)
    k +=1
    # print("="*30)
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score

    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
    all_comments = submission.comments.list()
    print("="*10 + " {}  comments   ".format(len(all_comments)))

    for c in all_comments[:min(10, len(all_comments))]:
        print("- {}".format(c.body))


1. open account on reddit
2. create app
3. auth to reddit

4. get new 10
    title, id, url,
5. get comments
