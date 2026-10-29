"""
Script crop ảnh tự động từ file thiết kế gốc 13072e44-4f5b-4d30-bedd-4ab70ee2a78f.jpg
cho dự án web Trekking Đi Cùng Gió.
"""

import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_PATH = os.path.join(BASE_DIR, '13072e44-4f5b-4d30-bedd-4ab70ee2a78f.jpg')
OUT_DIR = os.path.join(BASE_DIR, 'assets', 'images')

os.makedirs(OUT_DIR, exist_ok=True)

if not os.path.exists(IMAGE_PATH):
    print(f"Error: {IMAGE_PATH} does not exist.")
    exit(1)

mockup = Image.open(IMAGE_PATH)
w, h = mockup.size
print(f"Loaded design mockup image: {w}x{h}")

# 1. Hero banner (Nhóm 4 người đứng trên sống núi ngắm bình minh biển mây)
hero = mockup.crop((0, 68, 1214, 335))
hero.save(os.path.join(OUT_DIR, 'hero-banner.jpg'), quality=95)
print("Saved hero-banner.jpg:", hero.size)

# 2. Yen Tu (Mái Chùa Đồng cổ kính trên đỉnh núi đá giữa biển mây vàng rực lúc bình minh)
yen_tu = mockup.crop((73, 506, 263, 616))
yen_tu.save(os.path.join(OUT_DIR, 'yen-tu.jpg'), quality=95)
print("Saved yen-tu.jpg:", yen_tu.size)

# 3. Ta Xua (Biển mây trắng xóa cuồn cuộn phủ kín thung lũng và triền núi Tà Xùa)
ta_xua = mockup.crop((275, 506, 465, 616))
ta_xua.save(os.path.join(OUT_DIR, 'ta-xua.jpg'), quality=95)
print("Saved ta-xua.jpg:", ta_xua.size)

# 4. Phu Sa Phin (Sống núi cỏ xanh trùng điệp dưới bầu trời xanh và mây trắng Tây Bắc)
phu_sa_phin = mockup.crop((477, 506, 667, 616))
phu_sa_phin.save(os.path.join(OUT_DIR, 'phu-sa-phin.jpg'), quality=95)
print("Saved phu-sa-phin.jpg:", phu_sa_phin.size)

# 5. Ky Quan San (Sống lưng núi xanh mướt vươn cao hướng về đỉnh Kỳ Quan San)
ky_quan_san = mockup.crop((679, 506, 869, 616))
ky_quan_san.save(os.path.join(OUT_DIR, 'ky-quan-san.jpg'), quality=95)
print("Saved ky-quan-san.jpg:", ky_quan_san.size)

# 6. Video banner (Biển mây bồng bềnh giữa các tầng núi vùng cao Việt Nam)
video = mockup.crop((73, 774, 384, 960))
video.save(os.path.join(OUT_DIR, 'video-banner.jpg'), quality=95)
print("Saved video-banner.jpg:", video.size)

print("Done cropping all 6 base assets from original design!")
