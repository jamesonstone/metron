import csv
import requests
import os
import sqlite3

url = "https://api.yelp.com/v3/businesses/search"
api_key = os.environ.get("YELP_API_KEY")
headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
conn = sqlite3.connect("./dataset/businesses.db")  # create the database
c = conn.cursor()


def fetch(name, zipcode):
    """
    Fetches the first business from Yelp Fusion API based on the name and zip code; using best guess
    """
    params = {"term": name, "location": zipcode}  # business name  # zip code
    response = requests.get(url, headers=headers, params=params)

    # Check for a successful response
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Process and print the first business details
        if "businesses" in data and len(data["businesses"]) > 0:
            business = data["businesses"][0]
            return business
    else:
        print("Failed to retrieve data:", response.status_code)


def db_write(csv_row, yelp_data):
    """
    Writes the business data to the sqlite database,
    handling cases where yelp_data might be None.
    """

    if yelp_data is None:
        yelp_data = {}  # Create an empty dictionary for consistent handling

    c.execute(
        "INSERT INTO businesses VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            csv_row["name"] if csv_row["name"] else yelp_data.get("name", ""),
            ", ".join(yelp_data.get("location", {}).get("display_address", [])),
            csv_row["zip_code"]
            if csv_row["zip_code"]
            else yelp_data.get("location", {}).get("zip_code", ""),
            yelp_data.get("categories", [])[0].get("alias", "")
            if yelp_data.get("categories")
            else "",
            yelp_data.get("url", ""),
            str(yelp_data.get("is_closed", False)).lower(),
            csv_row["phone"] if csv_row["phone"] else yelp_data.get("phone", ""),
            yelp_data.get("rating", ""),
        ),
    )


def init_db():
    """
    Initializes the sqlite database
    """
    c.execute(
        """CREATE TABLE IF NOT EXISTS businesses
                 (name TEXT, address TEXT, zip_code TEXT, category TEXT, url TEXT,
                 is_closed TEXT, phone TEXT, rating INTEGER)"""
    )


def run():
    """
    Runs the data prep
    """
    init_db()
    with open("./dataset/business_lists.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], row["zip_code"])
            yelp_data = fetch(
                row["name"], row["zip_code"]
            )  # search yelp and take the first result
            db_write(row, yelp_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
