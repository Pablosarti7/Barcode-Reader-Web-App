import requests

def get_ingredient(ingredient):
    url = 'https://ingredients-api-t2ja.onrender.com/ingredients'
    parameters = {'name': ingredient}

    response = requests.get(url, params=parameters)

    data = response.json()
    
    if 'ingredient' in data:
        return data['ingredient'][0]
    else:
        return None
    
def add_ingredient(ingredient_object):
    add_url = 'https://ingredients-api-t2ja.onrender.com/add'
    headers = {
        "api-key": "secret_api_key",  # Replace with your actual API key
        "Content-Type": "application/json"
    }

    response = requests.post(add_url, headers=headers, json=ingredient_object)

    # Error handling
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        return f'HTTP error occurred: {err}'
    except Exception as err:
        return f'Other error occurred: {err}'
    