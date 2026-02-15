# 🎬 Letterboxd Wallpaper Generator

Create cinematic desktop wallpapers from your latest Letterboxd watches.

---

## ✨ What This Does

This script automatically:

* 🎬 Fetches your latest logged films from Letterboxd
* 🖼 Downloads high-quality poster images
* 🧱 Builds a cinematic **brick-style collage**
* 🌑 Applies a dark aesthetic background
* 🖥 Sets it as your desktop wallpaper

---

## 🖼 Example Output

![OutputImage](movie_wallpaper_brick.jpg)

---

## 🚀 Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/letterboxd-wallpaper.git
cd letterboxd-wallpaper
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

### 🔧 Step 1 — Add your Letterboxd username

Open the script and edit:

```python
USERNAME = "your_letterboxd_username"
```

### ▶ Step 2 — Run the script

```bash
python wallpaper.py
```

---

## 🖥 Result

✔ Wallpaper generated
✔ Saved in project folder
✔ Automatically set as desktop wallpaper (Windows)

---

## 🧱 Layout Style

The collage uses a **brick staggered layout** for a cinematic look:

```
[]    []
[] [] [] []
[] [] [] []
[] [] [] []
   []    []
```

✔ No empty space
✔ No rigid grid
✔ Natural poster flow

---

## 🛠 Requirements

* Python 3.8+
* Windows OS (for auto wallpaper setting)
* Internet connection

---

## 📦 Dependencies

* feedparser
* requests
* Pillow

Install manually if needed:

```bash
pip install feedparser requests pillow
```

---

## 🎨 Customization

You can easily modify:

* number of movies fetched
* poster resolution
* background color
* collage layout
* output filename

---

## 🧠 How It Works

1. Reads your Letterboxd RSS feed
2. Extracts poster images
3. Downloads high-resolution posters
4. Builds a staggered collage
5. Saves & sets wallpaper

---

## 🔮 Future Ideas

* IMDb support
* Movie title overlays
* Netflix-style UI layout
* Blur background aesthetic
* Daily auto-update wallpaper
* Animated slideshow mode

---

## ❤️ Author

**Lakshya Deewan**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍿 Share with movie lovers
* 🛠 Contribute improvements

---

## 📜 License

MIT License — free to use and modify.

---
