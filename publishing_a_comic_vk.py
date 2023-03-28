import os
from pathlib import Path
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
from random import randint


def get_random_comic():
    random_comic = randint(1, 2755)
    return random_comic


def download_comic(random_comic, safe_folder):
    os.makedirs(safe_folder, exist_ok=True)
    comic_links = f'https://xkcd.com/{random_comic}/info.0.json'
    response = requests.get(comic_links)
    response.raise_for_status()
    comic_image = response.json()
    images = comic_image.get('img')
    alt = comic_image.get('alt')
    path = urlparse(images).path
    extension = os.path.splitext(path)[1]
    image_name = f'comic_{extension}'
    get_comic = requests.get(images)
    filename = os.path.join(safe_folder, image_name)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(get_comic.content)
    return alt


def get_wall_upload_server():
    api_url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': os.getenv('access_token'),
        'v': 5.131,
    }
    response = requests.get(api_url, params=params)
    response_json = response.json()
    upload_url = response_json.get('response').get('upload_url')
    return upload_url


def upload_image(upload_url):
    path = Path('images/comic_.png')
    with open(path, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        upload_image_data = response.json()
    return upload_image_data


def save_wall_photo(upload_image_data):
    hash = upload_image_data.get('hash')
    server = upload_image_data.get('server')
    photo = upload_image_data['photo']
    params = {
        'access_token': os.getenv('access_token'),
        'hash': hash,
        'server': server,
        'photo': photo,
        'v': 5.131,
    }
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    response = requests.post(url, params=params)
    response.raise_for_status()
    photo_data = response.json()
    image_id = photo_data['response'][0].get('id')
    owner_id = photo_data['response'][0].get('owner_id')
    return image_id, owner_id


def wall_post(alt, image_id, owner_id):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': os.getenv('access_token'),
        'v': 5.131,
        'group_id': 219620053,
        'owner_id': -219620053,
        'from_group': 1,
        'message': alt,
        'attachments': f'photo{owner_id}_{image_id}'
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    os.remove('images/comic_.png')


def main():
    load_dotenv()
    safe_folder = Path('../images')
    random_comic = get_random_comic()
    alt = download_comic(random_comic, safe_folder)
    upload_url = get_wall_upload_server()
    upload_image_data = upload_image(upload_url)
    image_id, owner_id = save_wall_photo(upload_image_data)
    wall_post(alt, image_id, owner_id)
    get_random_comic()


if __name__ == '__main__':
    main()
