import json
import os

DATA_FILE = "src/data/reviews.json"

def save_review(review_data):

    if not os.path.exists(DATA_FILE):

        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:

        data = json.load(f)

    data.append(review_data)

    with open(DATA_FILE, "w") as f:

        json.dump(data, f, indent=4)


def load_reviews():

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:

        return json.load(f)