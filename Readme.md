# Google Photos Downloader with SQLite Tracking

This Python project allows you to download photos from your Google Photos account and track the downloads using an SQLite database. It stores the photo ID and metadata in the database to ensure that already downloaded photos are not re-downloaded.

## Features

- **Google Photos API Integration**: Fetch photos from your Google Photos account using OAuth 2.0 authentication.
- **SQLite Database Tracking**: Store photo IDs and filenames in a local SQLite database to track downloaded images.
- **Metadata Handling**: Downloads only the image files to a folder (`photos/`) and tracks their metadata in the SQLite database.
- **Pagination**: Handles API pagination to ensure that all photos are fetched from the library, not just the first batch.

## Prerequisites

- Python 3.x
- A Google Cloud project with the **Google Photos Library API** enabled.
- `credentials.json` from Google API Console.

### Required Python Libraries

You will need the following Python libraries to run this project:

```bash
pip install requests google-auth google-auth-oauthlib google-auth-httplib2 pillow
```

## Setup Instructions

### 1. Google API Setup

1. Go to the [Google API Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Google Photos Library API** for your project.
4. Set up OAuth 2.0 credentials and download the `credentials.json` file.
5. Place `credentials.json` in the root directory of the project.

### 2. Project Setup

1. Clone this repository or download the source code.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script to start downloading photos:
   ```bash
   python main.py
   ```

### Folder Structure

```
/google_photos_downloader
    ├── auth.py            # Handles Google OAuth 2.0 authentication
    ├── download.py        # Downloads photos from Google Photos
    ├── database.py        # Manages SQLite database interactions
    ├── metadata.py        # Optional module for metadata handling (currently unused)
    ├── main.py            # Main script to download photos and track them
    ├── photos/            # Folder where downloaded images will be saved (by default)
    ├── credentials.json   # Google API OAuth 2.0 credentials
    └── photos.db          # SQLite database to track downloaded photos
```

## Usage

### 1. Run the Project

Simply run the `main.py` file:

```bash
python main.py
```

The script will:

- Authenticate with the Google Photos API.
- Fetch all photos from your Google Photos account.
- Download photos to the `photos/` folder.
- Store the photo ID, filename, and download status in the SQLite database (`photos.db`).

### 2. Checking the Database

The `photos.db` SQLite database keeps track of all the photos you've downloaded, ensuring you don't download duplicates.

You can use SQLite tools to inspect the database:

```bash
sqlite3 photos.db
```

## Error Handling

- **Authentication Issues**: If there are issues with OAuth authentication, make sure that the `credentials.json` file is correct and that the token (`token.json`) is being generated properly.
- **Download Failures**: If a photo fails to download, it will be marked as `Failed` in the database.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Notes:

- [Mit License](https://opensource.org/license/mit)
- @meteor314
