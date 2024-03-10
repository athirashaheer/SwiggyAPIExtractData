# Swiggy Menu Extractor Using PowerShell

This PowerShell script extracts the menu/dish details from the Swiggy public API.

## Usage

To use the script, you need to supply the restaurant ID as an argument when running the script. The restaurant ID can be found by visiting the Swiggy app. For example, if the restaurant ID is 37968, you would run:

```sh
& .\SwiggyMenuExtract.ps1 -restaurantId 37968

```

This will create a CSV file with the menu details in the current directory. The file will be named **menu_data_<restaurant_id>.CSV**.
