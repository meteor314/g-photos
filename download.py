# download.py
import requests


def get_photos(creds):
    photos = []
    url = "https://photoslibrary.googleapis.com/v1/mediaItems"
    headers = {
        'Authorization': f'Bearer {creds.token}'
    }
    params = {

        'pageSize': 100  # pagination
    }

    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            media_items = data.get('mediaItems', [])
            photos.extend(media_items)

            next_page_token = data.get('nextPageToken')
            if next_page_token:
                params['pageToken'] = next_page_token
            else:
                url = None  # end of pagination
        else:
            raise Exception(f"Error fetching photos: {response.status_code}")

    return photos


def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return True
    return False
