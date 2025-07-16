
from constants import MAX_COMMENTS
from reddit.reddit import Reddit


def main():
    """
    The process of the application is as follows:
    1) Given a product name (query), call the Reddit API and search for comments reviewing the product
    2) Collect the review comments and sort them based on relevance, sentimence, and usefulness
    3) Analyze the top comments and return a list of the pros and cons of the product
    """

    # Make a new instance of Reddit in order to access the API
    scraper = Reddit(MAX_COMMENTS)

    # Query the user
    search_term = input("Enter the product to search for reviews: ")

    # Collect comments and save them
    comments = scraper.search_comments(search_term)
    scraper.save_to_json(comments, search_term)