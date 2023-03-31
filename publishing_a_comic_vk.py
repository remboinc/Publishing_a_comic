import os
from pathlib import Path
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
from random import randint


def get_random_comics_number():
    first_comic_number = 1
    last_comic_number = 2755
    random_comics_number = randint(first_comic_number, last_comic_number)
    return random_comics_number


def download_comic(random_comics_number, сomic_book_folder):
    os.makedirs(сomic_book_folder, exist_ok=True)
    comic_link = f'https://xkcd.com/{random_comics_number}/info.0.json'
    response = requests.get(comic_link)
    response.raise_for_status()
    all_about_comic = response.json()
    image = all_about_comic.get('img')
    alt = all_about_comic.get('alt')
    path = urlparse(image).path
    extension = os.path.splitext(path)[1]
    image_name = f'comic_{extension}'
    comic = requests.get(image)
    filename = os.path.join(сomic_book_folder, image_name)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(comic.content)
    return alt


def get_wall_upload_server(access_token, api_version):
    api_url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': access_token,
        'v': api_version,
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    upload_url = response.json().get('response').get('upload_url')
    return upload_url


def upload_image(upload_url):
    path = Path('images/comic_.png')
    with open(path, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
    response.raise_for_status()
    uploaded_image = response.json()
    return uploaded_image


def save_wall_photo(uploaded_image, access_token, api_version):
    hash_ = uploaded_image.get('hash')
    server = uploaded_image.get('server')
    photo = uploaded_image['photo']
    params = {
        'access_token': access_token,
        'hash': hash_,
        'server': server,
        'photo': photo,
        'v': api_version,
    }
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    response = requests.post(url, params=params)
    response.raise_for_status()
    image_id = response.json()['response'][0].get('id')
    owner_id = response.json()['response'][0].get('owner_id')
    return image_id, owner_id


def wall_post(alt, image_id, owner_id, access_token, api_version):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': 219620053,
        'owner_id': -219620053,
        'from_group': 1,
        'message': alt,
        'attachments': f'photo{owner_id}_{image_id}'
    }
    response = requests.post(url, params=params)
    response.raise_for_status()


def deleted_published_comic():
    os.remove('images/comic_.png')


def main():
    load_dotenv()
    access_token = os.getenv('ACCESS_TOKEN')
    api_version = 5.131
    сomic_book_folder = Path('images')

    random_comics_number = get_random_comics_number()
    alt = download_comic(random_comics_number, сomic_book_folder)
    upload_url = get_wall_upload_server(access_token, api_version)
    uploaded_image = upload_image(upload_url)
    image_id, owner_id = save_wall_photo(uploaded_image, access_token, api_version)
    wall_post(alt, image_id, owner_id, access_token, api_version)
    deleted_published_comic()


if __name__ == '__main__':
    main()
