# Import the required Modules
import requests
import pandas as pd
import sys

# Function to fetch menu data from Swiggy's API
def fetch_menu_data(restaurant_id):
    # Header for avoid 403 error
    # The User-Agent is an HTTP header that identifies the client (usually a web browser or a script) making the request.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/18.18362"
    }
    url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for restaurant_id: {restaurant_id}")
        print(f"Error: {e}")
        return None
    return response.json()

# Recursive function to find menu items in JSON data
def find_menu_items(d, menu_items):
    if isinstance(d, dict):
        for k, v in d.items():
            if k == "@type" and v == "type.googleapis.com/swiggy.presentation.food.v2.Dish":
                menu_items.append(d)
            else:
                find_menu_items(v, menu_items)
    elif isinstance(d, list):
        for item in d:
            find_menu_items(item, menu_items)

# Function to parse the JSON data and extract menu items
def parse_json(data):
    menu_items = []
    find_menu_items(data, menu_items)
    return menu_items

# Function to convert menu items to a DataFrame
def menu_items_to_df(menu_items):
    data = []
    for item in menu_items:
        info = item.get('info', {})
        data.append({
            'name': info.get('name'),
            'category': info.get('category'),
            'description': info.get('description'),
            'price': info.get('price')
        })
    df = pd.DataFrame(data)
    return df

# Main function to fetch, parse, and export data
def main(restaurant_id):
    data = fetch_menu_data(restaurant_id)
    if data is not None:
        menu_items = parse_json(data)
        df = menu_items_to_df(menu_items)
        try:
            df.to_csv(f'menu_data_{restaurant_id}.csv', index=False)
            print(f"Menu data has been exported to menu_data_{restaurant_id}.csv")
        except Exception as e:
            print(f"Failed to export data to CSV file. Error: {e}")

# Command-line argument for restaurant_id
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <restaurant_id>")
        sys.exit(1)
    restaurant_id = sys.argv[1]
    main(restaurant_id)
