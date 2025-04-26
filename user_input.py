from reddit_search import search_subreddit_titles, search_subreddit_content
from predictor import predict_emotion
query = input("Enter a search query: ")
num_posts = int(input("Enter the number of posts to retrieve: "))
post_type = input("Do you want to search the reddit posts by title or content? (Enter 'title' or 'content'): ")
if post_type.lower() == 'title':
    posts = search_subreddit_titles(query, num_posts)
elif post_type.lower() == 'content':
    posts = search_subreddit_content(query, num_posts)
else:
    raise ValueError("Invalid input. Please enter 'title' or 'content'.")

if __name__ == "__main__":
    emotion_counts = predict_emotion(posts)
    messages = [f"{count} instances of {emotion} text" for emotion, count in emotion_counts.items()]

    if len(messages) > 1:
        final_message = ", ".join(messages[:-1]) + ", and " + messages[-1] + f" when you searched '{query}' in all subreddits limited to the top {num_posts} results."
    else:
        final_message = messages[0] + f" when you searched '{query}' in all subreddits limited to the top {num_posts} results."
    print("There were " + final_message)



