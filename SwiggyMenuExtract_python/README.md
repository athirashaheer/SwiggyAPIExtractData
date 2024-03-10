# Swiggy Menu Extractor Using Python

This Python script extracts the menu/dish details from the Swiggy public API.

## Prerequisites

The following Python modules are required for this script to function properly. These modules are also listed in the `requirements.txt` file:

- **requests**
- **pandas**

## Installation

The installation of these modules is a one-time task required for the script to work. You can install them by running the following commands in your command line or shell:

```sh
pip install requests
pip install pandas
```

## Usage

To use the script, you need to supply the restaurant ID as an argument when running the script. The restaurant ID can be found by visiting the Swiggy app. For example, if the restaurant ID is 37968, you would run:

```sh
python .\SwiggyMenuExtract.py 37968

```

This will create a CSV file with the menu details in the current directory. The file will be named **menu_data_<restaurant_id>.CSV**.
