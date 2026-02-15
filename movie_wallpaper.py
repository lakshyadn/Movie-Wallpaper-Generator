import feedparser
import requests
from PIL import Image
from io import BytesIO
import re
import random

USERNAME = "lakshyadeewan"
NUM_MOVIES = 36

rss_url = f"https://letterboxd.com/{USERNAME}/rss/"
feed = feedparser.parse(rss_url)

headers = {
    "User-Agent": "Mozilla/5.0"
}

posters = []

for entry in feed.entries[:NUM_MOVIES]:

    description = entry.description
    match = re.search(r'<img src="(.*?)"', description)

    if not match:
        continue

    poster_url = match.group(1)

    try:
        response = requests.get(poster_url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("Skipping (bad response):", poster_url)
            continue

        img = Image.open(BytesIO(response.content)).convert("RGB")
        posters.append(img)

        # print("Downloaded:", poster_url)

    except Exception as e:
        print("Skipping broken image:", e)

if not posters:
    print("No posters downloaded.")
    exit()

# resize posters
base_size = (500, 750)
posters = [p.resize(base_size) for p in posters]

# create collage with brick pattern (shift every 3 columns)
cols_per_row = 9
rows_needed = (len(posters) + cols_per_row - 1) // cols_per_row
canvas_width = cols_per_row * base_size[0]
canvas_height = rows_needed * base_size[1] + 150  # +150 for the max shift

wallpaper = Image.new('RGB', (canvas_width, canvas_height), (20, 20, 20))

# Generate column offsets: pattern repeats every 3 columns
column_offsets = []
shift_down = 100
shift_pattern = [0, shift_down, shift_down * 2]  # col 0: normal, col 1: shift, col 2: shift more
for col in range(cols_per_row):
    column_offsets.append(shift_pattern[col % 3])

for i, poster in enumerate(posters):
    # Regular grid positioning
    row = i // cols_per_row
    col = i % cols_per_row
    
    # Each column has a fixed offset, no spacing between posters
    x_pos = col * base_size[0]
    y_pos = row * base_size[1] + column_offsets[col]
    
    wallpaper.paste(poster, (x_pos, y_pos))

# Crop to remove excess black space at the bottom
def find_bottom_edge(img):
    """Find the lowest non-black pixel"""
    pixels = img.load()
    max_y = 0
    for y in range(img.height - 1, -1, -1):
        for x in range(img.width):
            if pixels[x, y] != (20, 20, 20):
                return y
    return img.height

bottom = find_bottom_edge(wallpaper)
wallpaper = wallpaper.crop((0, 0, canvas_width, bottom + 1))

wallpaper.save("movie_wallpaper_brick.jpg", quality=95)

print("\n✅ Wallpaper created successfully!")


#Automation
import ctypes
import os

# save path
output_path = os.path.abspath("movie_wallpaper_brick.jpg")

# set as wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, output_path, 3)

print("🎬 Wallpaper applied!")
