import os
import random
import requests

def get_image_url_full():
    image_url = 'https://raw.githubusercontent.com/Sstudios-Dev/image-core/main/src/img/'
    random_number = random.randint(1, 46)  # Assuming there are 46 images
    image_name = f'img-core{random_number}.jpg'
    return {'image_url_full': f'{image_url}{image_name}?raw=true', 'image_name': image_name}

def download_random_image():
    image_info = get_image_url_full()
    image_url_full = image_info['image_url_full']
    image_name = image_info['image_name']
    directory = './images-Random'

    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        response = requests.get(image_url_full)
        with open(os.path.join(directory, image_name), 'wb') as f:
            f.write(response.content)
        print(f'Random image {image_name} downloaded')
    except Exception as e:
        print(f'Failed to download image {image_name}: {str(e)}')

if __name__ == "__main__":
    download_random_image()
