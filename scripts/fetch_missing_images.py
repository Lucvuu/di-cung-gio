import urllib.request, ssl, sys, os
from PIL import Image, ImageOps
import io
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# High quality curated images matching exact Vietnam topography:
# Sa Mu (mossy forest, enchanted primeval trees)
# Cửa Tử (tropical canyon waterfall stream)
# Cúc Phương (primeval forest, butterfly jungle)
# Đà Giang (emerald lake & limestone mountains, like Da River / Hoa Binh)
# Lùng Cúng (majestic grassy mountain peak with sunrise clouds)
# Nhìu Cồ San (misty waterfall and bamboo mountain forest)
# Fansipan (highest peak in Indochina)
# Ngọa Vân (ancient pagoda atop green mountain mist)

image_urls = {
    'tour-samu.jpg': 'https://images.unsplash.com/photo-1511497584788-87676104235f?w=1000&q=85', # dense mystical misty forest with moss & ancient trees
    'tour-cua-tu.jpg': 'https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=1000&q=85', # clear jungle river stream with boulders
    'tour-cuc-phuong.jpg': 'https://images.unsplash.com/photo-1448375240586-882707db888b?w=1000&q=85', # deep primeval forest canopy
    'tour-da-giang.jpg': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1000&q=85', # tranquil emerald waters and lush mountain islands
    'tour-lung-cung.jpg': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1000&q=85', # high alpine mountain peak overlooking clouds
    'tour-nhiu-co-san.jpg': 'https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?w=1000&q=85', # majestic waterfall pouring into mountain stream
    'tour-fansipan.jpg': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1000&q=85', # rocky sharp mountain summit piercing above clouds
    'tour-ngoa-van.jpg': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1000&q=85', # peaceful mountain temple roof in mist
}

for fname, url in image_urls.items():
    out_path = os.path.join('assets/images', fname)
    if os.path.exists(out_path):
        print(f"Skipping {fname}, already exists.")
        continue
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            # Crop to 4:3 (800x600)
            target_w, target_h = 800, 600
            aspect = target_w / target_h
            w, h = im.size
            if w / h > aspect:
                new_w = int(h * aspect)
                left = (w - new_w) // 2
                crop_box = (left, 0, left + new_w, h)
            else:
                new_h = int(w / aspect)
                top = (h - new_h) // 2
                crop_box = (0, top, w, top + new_h)
            cropped = im.crop(crop_box).resize((target_w, target_h), Image.Resampling.LANCZOS)
            cropped.save(out_path, 'JPEG', quality=88)
            print(f"Successfully saved {fname} (800x600)")
    except Exception as e:
        print(f"Failed to download {fname}: {e}")

