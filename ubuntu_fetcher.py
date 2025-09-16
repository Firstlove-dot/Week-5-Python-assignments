"""
Ubuntu-Inspired Image Fetcher
"I am because we are" – A mindful tool for collecting images from the web.
"""

import requests
import os
import hashlib
from urllib.parse import urlparse

# Directory to store images
IMAGE_DIR = "Fetched_Images"
# Keep track of downloaded content hashes to avoid duplicates
downloaded_hashes = set()

def fetch_image(url):
    try:
        # Ensure directory exists
        os.makedirs(IMAGE_DIR, exist_ok=True)

        # Request image (stream to control large files)
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check Content-Type header for images
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Optional size limit check
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 10 * 1024 * 1024:  # 10MB
            print(f"✗ Skipped (too large >10MB): {url}")
            return

        # Download content into memory
        content = response.content

        # Check duplicate by content hash
        content_hash = hashlib.md5(content).hexdigest()
        if content_hash in downloaded_hashes:
            print(f"⚠ Already downloaded identical image from {url}, skipping.")
            return
        downloaded_hashes.add(content_hash)

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = f"downloaded_image_{content_hash[:8]}.jpg"

        filepath = os.path.join(IMAGE_DIR, filename)

        # Save the image
        with open(filepath, "wb") as f:
            f.write(content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("Mindfully collecting images from the web\n")

    urls = input("Please enter image URLs separated by commas:\n").split(",")
    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
