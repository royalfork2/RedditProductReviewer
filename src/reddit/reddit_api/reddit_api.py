import praw
import os

from src.reddit.reddit_api.constants import CLIENT_ID, CLIENT_SECRET, PASSWORD, USER_AGENT, USERNAME


class RedditAPI:
    def __init__(self):
        self.reddit_api = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            username=USERNAME,
            password=PASSWORD,
            user_agent=USER_AGENT
        )

    def search_comments(self, query, max_comments):
        """
        Call the Reddit API to search comments related to query
        """
        comments_collected = []
        for submission in self.reddit_api.subreddit("all").search(query, limit=10):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                if len(comments_collected) >= max_comments:
                    break
                comments_collected.append(
                    {
                        "post_title": submission.title,
                        "comment_body": comment.body,
                        "score": comment.score,
                        "permalink": f"https://www.reddit.com{comment.permalink}",
                    }
                )
            if len(comments_collected) >= max_comments:
                break
        return comments_collected
