from dotenv import load_dotenv
import os
import praw
load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

def search_subreddit_titles(query, num_posts=1):
    subreddit = reddit.subreddit('all')
    posts = subreddit.search(query, limit=num_posts)
    filtered = []
    for post in posts:
        filtered.append(post.title)
    filtered_list = [item for item in filtered if item != ""]
    for i in range(len(filtered_list)):
        filtered_list[i] = filtered_list[i].replace('\n', '')
    return filtered_list
def search_subreddit_content(query, num_posts=1):
    subreddit = reddit.subreddit('all')
    posts = subreddit.search(query, limit=num_posts)
    filtered = []
    for post in posts:
        filtered.append(post.selftext)
    filtered_list = [item for item in filtered if item != ""]
    for i in range(len(filtered_list)):
        filtered_list[i] = filtered_list[i].replace('\n', '')
    return filtered_list
if __name__ == "__main__":
   #print(search_subreddit_titles("trump", num_posts=3))
   print(search_subreddit_content("trump", num_posts=3))