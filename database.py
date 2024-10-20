# database.py
import sqlite3


def create_database():
    conn = sqlite3.connect('photos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS photos (
            id TEXT PRIMARY KEY,
            filename TEXT,
            download_status TEXT
        )
    ''')
    conn.commit()
    conn.close()


def insert_photo(id, filename, status):
    conn = sqlite3.connect('photos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO photos (id, filename, download_status)
        VALUES (?, ?, ?)
    ''', (id, filename, status))
    conn.commit()
    conn.close()


def is_photo_downloaded(id):
    conn = sqlite3.connect('photos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM photos WHERE id = ?', (id,))
    photo = cursor.fetchone()
    conn.close()
    return photo is not None
