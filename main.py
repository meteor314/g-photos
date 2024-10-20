# main.py
import os
from auth import authenticate
from download import get_photos, download_image
from database import create_database, insert_photo, is_photo_downloaded
import sqlite3

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


    # download all failed images 
    print("Downloading failed images")

    failed_images = get_failed_images()
    for failed_image in failed_images:
        photo_id = failed_image[0]
        filename = failed_image[1]

        base_url = f"https://photoslibrary.googleapis.com/v1/mediaItems/{photo_id}"

        if download_image(base_url, filename):
            print(f"Photo {photo_id} downloaded successfully.")
            insert_photo(photo_id, filename, 'Downloaded')
        else:
            print(f"Failed to download photo {photo_id}.")
            insert_photo(photo_id, filename, 'Failed')


def get_failed_images():


    conn = sqlite3.connect('photos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM photos WHERE status = 'Failed'")
    failed_images = cursor.fetchall()

    conn.close()

    return failed_images

if __name__ == '__main__':
    main()
