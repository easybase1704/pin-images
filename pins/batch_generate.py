#!/usr/bin/env python3
"""批量生成Pinterest Pin图 - 白底简洁风"""
from PIL import Image, ImageDraw, ImageFont
import os

RAW = r"C:\Users\rb\pin-images\pins\raw"
OUT = r"C:\Users\rb\pin-images\pins\batch"
FONTS = r"C:\Windows\Fonts"
os.makedirs(OUT, exist_ok=True)

W, H = 564, 1002

# 产品数据: [文件名, 中文名, 英文标题(用于文件名)]
products = [
    # 已有图片的产品
    ("drawer_dividers.jpg", "adjustable-drawer-dividers"),
    ("cable_tray.jpg", "under-desk-cable-management"),
    ("monitor_stand.jpg", "monitor-stand-riser"),
    ("bathroom_shelf.jpg", "no-drill-bathroom-shelf"),
    ("rattan_basket.jpg", "rattan-bathroom-basket"),
]

def make_pin(img_file, name):
    """生成单张Pin图"""
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # 加载产品图
    path = os.path.join(RAW, img_file)
    if not os.path.exists(path):
        print(f"  SKIP {img_file}")
        return None

    pi = Image.open(path).convert("RGBA")
    # 放大产品，撑满画面宽度
    nw = W - 40
    nh = int(pi.height * (nw / pi.width))
    if nh > 850:
        nh = 850
        nw = int(pi.width * (nh / pi.height))
    pi = pi.resize((nw, nh), Image.LANCZOS)

    # 产品居中
    img.paste(pi, ((W - nw)//2, 80), pi)

    # 底部深色半透明条
    bar = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bar)
    bd.rectangle([(0, H-80), (W, H)], fill=(0, 0, 0, 80))
    img_rgba = img.convert("RGBA")
    img_rgba.paste(bar, (0, 0), bar)
    img = img_rgba.convert("RGB")
    draw = ImageDraw.Draw(img)

    # 品牌字
    arial = ImageFont.truetype(os.path.join(FONTS, "arial.ttf"), 14)
    yh = ImageFont.truetype(os.path.join(FONTS, "msyh.ttc"), 13)
    draw.text((20, 935), "Amazon Finds", fill="#FFFFFF", font=arial)

    save_name = f"{name}_amazon_finds_pin.jpg"
    save_path = os.path.join(OUT, save_name)
    img.save(save_path, "JPEG", quality=92)
    return save_name

print("Generating pins...")
count = 0
for img_file, name in products:
    result = make_pin(img_file, name)
    if result:
        print(f"  OK {result}")
        count += 1

print(f"\nDone! Generated {count} pins in {OUT}")
