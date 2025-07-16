import json

from src.reddit.reddit_api.reddit_api import RedditAPI


class Reddit:
    def __init__(self, max_comments=50):
        # Initalize the API
        self.api = RedditAPI()
        self.max_comments = max_comments

    def search_comments(self, product_name):
        """
        Query the Reddit API to search for relevant comments
        """
        return self.api.search_comments(product_name, self.max_comments)

    def convert_to_json(self, comments: list, product_name: str):
        """
        Save the comments in a well formatted json file

        Args:
            - comments (list): comments found from API call
            - product_name (str): name of the product
        """
        filename = f"{product_name.replace(' ', '_')}_reddit_reviews.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        # Print the found comments into a file
        print(f"Saved {len(comments)} comments to {filename}")

    scraper = RedditReviewScraper(max_comments=100)
    search_term = input("Enter the product to search for reviews: ")
    comments = scraper.search_and_collect_comments(search_term)
    scraper.save_to_json(comments, search_term)

