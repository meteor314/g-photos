# main.py
import os
from auth import authenticate
from download import get_photos, download_image
from database import create_database, insert_photo, is_photo_downloaded


def main():
    creds = authenticate()

    create_database()

    if not os.path.exists('photos'):
        os.makedirs('photos')

    photos = get_photos(creds)

    for photo in photos:
        photo_id = photo['id']
        filename = f"photos/{photo_id}.jpg"

        if is_photo_downloaded(photo_id):
            print(f"Photo {photo_id} already downloaded, skipping.")
            continue

        base_url = photo['baseUrl'] + "=d"  # uri for downloading  images

        if download_image(base_url, filename):
            print(f"Photo {photo_id} downloaded successfully.")

            insert_photo(photo_id, filename, 'Downloaded')
        else:
            print(f"Failed to download photo {photo_id}.")
            insert_photo(photo_id, filename, 'Failed')  # status of download


if __name__ == '__main__':
    main()
