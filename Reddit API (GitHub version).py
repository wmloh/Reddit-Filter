import praw

reddit = praw.Reddit(client_id='clientid',
                     client_secret='clientsecret',
                     username='username',
                     password='password',
                     user_agent='useragent')


def subm_and_comm(subred, lim):
    subreddit = reddit.subreddit(subred)
    category = subreddit.hot(limit=lim)

    for submission in category:
        if not submission.stickied:
            print('Title: {}\nups: {}\ndowns: {}\nby: {}\n'.format(submission.title,
                                                                   submission.ups,
                                                                   submission.downs,
                                                                   submission.author))
            comments = submission.comments
            for comment in comments:
                print("Comment by " + str(comment.author) + ": " + comment.body)

def stream_comment(subred):
    subreddit = reddit.subreddit(subred)
    
    for comment in subreddit.stream.comments():
        try:
            print("Comment by " + str(comment.author) + ": " + comment.body)
        except Exception as e:
            pass

def stream_submissions(subred):
    subreddit = reddit.subreddit(subred)
    for submission in subreddit.stream.submissions():
        try:
            print("Post by " + str(submission.author) + ": " + submission.title)
        except Exception as e:
            pass

def filter_sub(substr, subred, count=False):
    counter = 0
    
    subreddit = reddit.subreddit(subred)
    if count:
        for submission in subreddit.submissions():
            try:
                post = submission.title
                if substr in post:
                    counter += 1
                    print(counter)
            except Exception as e:
                pass
    else:
        for submission in subreddit.submissions():
            try:
                post = submission.title
                if substr in post:
                    print("Post by " + str(submission.author) + ": " + submission.title)
            except Exception as e:
                pass

def filter_user(user, subred, count=False):
    counter = 0

    subreddit = reddit.subreddit(subred)
    if count:
        for submission in subreddit.submissions():
            try:
                if submission.author == user:
                    counter += 1
                    print(counter)
            except Exception as e:
                pass
    else:
        for submission in subreddit.submissions():
            try:
                if submission.author == user:
                    print("Post by " + str(submission.author) + ": " + submission.title)
            except Exception as e:
                pass
                
