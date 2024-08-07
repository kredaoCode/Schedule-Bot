import requests

token = 'vk1.a.r8ndRoCn4h9RNzgp_qh41hLo6dHfSg0KAJygTtFuZqPF3PyJ5DKykYfvbd8X2r6CrUsWGBrhsrnLLJEIzhHAUSdSS0yX7f7Yzaxgsd-uhCvcndpW9dwNcvHOSPMxCDo9som1fqzMNGhbJiu9cmtRWI6XbTQughjy9RHWAN4RE5zLGz8TGcXoKR6gjZekYeqh7nDMHV8VKp9d7NcI0f2ycA'


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