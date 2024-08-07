import requests

import TOKEN

token = TOKEN.token


def get_images():
    response = requests.get(
        'https://api.vk.com/method/wall.get',
        params={
            'access_token': token,
            'domain': 'couples_schedul',
            'v': 5.199,
            'count': 100
        }
    )
    response.json()

    def has_photo(items):
        return any(item.get("type") == "photo" for item in items)

    content = response.json()['response']['items']
    content = [item for item in content if
               "copy_history" not in item and item.get("text") == "" and has_photo(item.get("attachments", []))]

    return [item['photo'] for entry in content for item in entry.get("attachments", [])]

print(get_images())