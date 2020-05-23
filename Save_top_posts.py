import praw, praw.models
import os
import sys

# Fill in with API key data from https://www.reddit.com/prefs/apps
CLIENT_ID = ''
CLIENT_SECRET = ''
USER_AGENT = ''
DEFAULT_NUM_POSTS = 25
DEFAULT_NUM_COMMENTS = 25
BLOCKED_CHARS = ['<', '>', ':', '"', '/', r'"\"', '|', '?', '.']
''' 
    This function returns a list of dictionaries containing the best rated 
    comments from the passed in post. The dictionary has the keys comment
    and author which stores the comments post and comments author respectively  
    
    :param post: The post object you which to get the best comments for
    :param count: The number of comments you want returned back to you

'''
def get_best_comments(post, count):
    # Define the why you want the comments sorted
    post.comment_sort = 'best'
    # set passed in argument for count to the limit of comments to return
    post.comment_limit = count
    # list to store the sorted comments
    return_comments  = [] 
    for top_level_comment in post.comments:
        if isinstance(top_level_comment, praw.models.MoreComments):
            continue
        # for each comment we are adding it as a dictionary to the return list
        return_comments.append({'comment': top_level_comment.body, 'author': \
             top_level_comment.author})
    return return_comments

'''
    This function saves the top posts and comments from each subreddit in there
    respective folder. 

    :param subreddits: A list that contains strings of the subreddits 
    :param num_posts: The number of posts you want to generate files for in each 
        subreddit
    :param num_comments: The number of comments to want to include in each file
'''
def save_top_posts_from_subreddit(subs, num_posts, num_comments):
    reddit = praw.Reddit(client_id=CLIENT_ID, \
    client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    try:
        os.mkdir(os.getcwd()+'/Posts/{}/'.format(sub))
    except FileExistsError:
        pass
    finally:
        hot_posts = reddit.subreddit(sub).hot(limit=num_posts)
        posts = []
        for post in hot_posts:
            posts.append({'title': post.title, 'creator': post.author,\
                'comments': get_best_comments(post, num_comments)})
        for data in posts:
            f = open(os.getcwd()+'/Posts/{}/'.format(sub) \
                + str(remove_special_char(data['title']))+ '.txt',"a")
            f.write('\t' + data['title'] + '\n' + 'Posted By: {}'.format(data['creator'])+'\n\n')     
            for comment in data['comments']:
                f.write(str(comment['comment'] + '\n'))
                f.write('\tPosted By: {} \n\n'.format(comment['author']))
            f.close()

def remove_special_char(title):
    return_string = title[:120]
    for char in BLOCKED_CHARS:
        return_string = return_string.replace(char, ' ')
    return return_string

if __name__ == "__main__":
    try:
        sub = sys.argv[1]
        print('Sub: {}, Number of Comments: {}, Number of Posts: {}'\
            .format(sub, DEFAULT_NUM_POSTS, DEFAULT_NUM_COMMENTS))
        save_top_posts_from_subreddit(sub, DEFAULT_NUM_POSTS, DEFAULT_NUM_COMMENTS)
    except IndexError:
        print('Please supply the required command line argument of a subreddit')
