import requests

from app.tokens import vk_token

token = vk_token

def get_url(content):
    image_urls = []
    
    for item in content:
        if 'attachments' in item:
            for attachment in item['attachments']:
                if attachment['type'] == 'photo':
                    for size in attachment['photo']['sizes']:
                        if size['type'] == 'w':
                            image_urls.append(size['url'])
    
    return image_urls
    

def get_images(last_date: int):
    response = requests.get(
        'https://api.vk.com/method/wall.get',
        params={
            'access_token': token,
            'domain': 'couples_schedul',
            'v': 5.199,
            'count': 100
        }
    )

    def has_photo(items):
        return any(item.get("type") == "photo" for item in items)
    
    print(response.json())

    content = response.json()['response']['items']
    content = [item for item in content if
               "copy_history" not in item and item.get("text") == "" and has_photo(item.get("attachments", []))]

    #return [item['photo'] for entry in content for item in entry.get("attachments", [])]
    if last_date == 0:
        return get_url([content[0]])
    else:
        return get_url([item for item in content if item['date'] > last_date])