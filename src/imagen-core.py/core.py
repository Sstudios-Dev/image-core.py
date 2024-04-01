import random
import requests
import os

def get_image_url_full():
    image_url = 'https://raw.githubusercontent.com/Sstudios-Dev/image-core/main/src/img/'
    random_number = random.randint(1, 70)  # Assuming there are 46 images
    image_name = f'img-core{random_number}.jpg'
    return {'image_url_full': f'{image_url}{image_name}?raw=true', 'image_name': image_name}

def download_random_image():
    data = get_image_url_full()
    image_url_full = data['image_url_full']
    image_name = data['image_name']
    directory = './images-random'

    if not os.path.exists(directory):
        os.mkdir(directory)

    try:
        response = requests.get(image_url_full)
        with open(os.path.join(directory, image_name), 'wb') as file:
            file.write(response.content)
        print(f'Image random {image_name} downloaded')
    except Exception as e:
        print(f'Failed to download image {image_name}: {e}')

if __name__ == '__main__':
    download_random_image()
