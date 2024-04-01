import random
import requests
import os

def get_random_anime_image_url():
    anime_image_url = 'https://raw.githubusercontent.com/Sstudios-Dev/image-core/main/src/img-anime/'
    random_number = random.randint(1, 200)  # Assuming there are 120 images
    image_name = f'img-anime{random_number}.jpg'
    return {'anime_image_url_full': f'{anime_image_url}{image_name}?raw=true', 'image_name': image_name}

def download_random_anime_image():
    data = get_random_anime_image_url()
    anime_image_url_full = data['anime_image_url_full']
    image_name = data['image_name']
    directory = './anime-images'

    if not os.path.exists(directory):
        os.mkdir(directory)

    try:
        response = requests.get(anime_image_url_full)
        with open(os.path.join(directory, image_name), 'wb') as file:
            file.write(response.content)
        print(f'Anime image {image_name} downloaded')
    except Exception as e:
        print(f'Failed to download image {image_name}: {e}')

if __name__ == '__main__':
    download_random_anime_image()
