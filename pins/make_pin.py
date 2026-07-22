#!/usr/bin/env python3
"""生成Pinterest Pin图 - 竖屏1000x1500"""
from PIL import Image, ImageDraw, ImageFont
import os, json

RAW = r"C:\Users\rb\pin-images\pins\raw"
OUT = r"C:\Users\rb\pin-images\pins"
os.makedirs(OUT, exist_ok=True)

W, H = 1000, 1500  # 2:3竖屏

def load_img(name, size=(400, 400)):
    """加载并裁剪产品图，去白边"""
    path = os.path.join(RAW, name)
    if not os.path.exists(path):
        print(f"  ⚠ 缺少 {name}")
        return None
    img = Image.open(path).convert("RGBA")
    # 缩放到目标尺寸
    img.thumbnail(size, Image.LANCZOS)
    return img

def rounded_rect(draw, xy, radius, fill):
    """画圆角矩形"""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill)

def create_pin_1():
    """Sample 1: Desk Organization Finds"""
    img = Image.new("RGB", (W, H), "#FAFAFA")
    draw = ImageDraw.Draw(img)

    # 背景装饰 - 浅灰色圆角区域
    rounded_rect(draw, (50, 50, 950, 1100), 30, "#FFFFFF")
    draw.rounded_rectangle([50, 1130, 950, 1450], 30, "#FFFFFF"])

    # Load fonts (try multiple options)
    font_title = None
    font_body = None
    for fp in [
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\Arial.ttf",
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\SegoeUI.ttf",
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\msyhbd.ttc",
    ]:
        if os.path.exists(fp):
            try:
                font_title = ImageFont.truetype(fp, 52)
                font_body = ImageFont.truetype(fp, 28)
                print(f"  Font loaded: {fp}")
                break
            except:
                continue

    if not font_title:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()

    # Title
    draw.text((100, 80), "Amazon", fill="#E60023", font=font_title)
    draw.text((100, 145), "Desk Organization", fill="#333333", font=ImageFont.truetype(
        [fp for fp in [r"C:\Windows\Fonts\arial.ttf",r"C:\Windows\Fonts\Arial.ttf"] if os.path.exists(fp)][0] if any(os.path.exists(fp) for fp in [r"C:\Windows\Fonts\arial.ttf",r"C:\Windows\Fonts\Arial.ttf"]) else None, 48) if font_title else font_title, 48))
    draw.text((100, 205), "Finds I Wish I Bought Sooner", fill="#666666", font=font_body)

    # Product grid (2x2)
    products = [
        ("drawer_dividers.jpg", 0, 0),
        ("cable_tray.jpg", 1, 0),
        ("monitor_stand.jpg", 0, 1),
        ("bathroom_shelf.jpg", 1, 1),
    ]

    grid_x, grid_y = 120, 300
    cell_w, cell_h = 370, 370
    gap = 30

    for fname, col, row in products:
        prod_img = load_img(fname)
        if prod_img:
            x = grid_x + col * (cell_w + gap)
            y = grid_y + row * (cell_h + gap)
            # Center in cell
            pw, ph = prod_img.size
            ox = x + (cell_w - pw) // 2
            oy = y + (cell_h - ph) // 2
            # White card behind
            draw.rounded_rectangle([x-10, y-10, x+cell_w+10, y+cell_h+10], 15, "#FFFFFF")
            draw.rounded_rectangle([x-8, y-8, x+cell_w+8, y+cell_h+8], 13, "#F5F5F5")
            img.paste(prod_img, (ox, oy), prod_img if prod_img.mode == "RGBA" else None)

    # Bottom CTA area
    draw.rounded_rectangle([80, 1160, 920, 1420], 20, "#E60023"])
    draw.text((120, 1200), "✨ 点主页链接购买", fill="#FFFFFF", font=font_body)
    draw.text((120, 1250), "✨ Shop at link in BI0", fill="#FFFFFF", font=font_body)
    draw.text((120, 1320), "#amazonfinds #deskorganization", fill="#FFD4D4", font=ImageFont.truetype(
        [fp for fp in [r"C:\Windows\Fonts\arial.ttf",r"C:\Windows\Fonts\Arial.ttf"] if os.path.exists(fp)][0] if any(os.path.exists(fp) for fp in [r"C:\Windows\Fonts\arial.ttf",r"C:\Windows\Fonts\Arial.ttf"]) else None, 24) if font_body else font_body, 24))

    save_path = os.path.join(OUT, "desk_org_finds_01.jpg")
    img.save(save_path, "JPEG", quality=92)
    print(f"\n✅ 样图已保存: {save_path}")
    return save_path

if __name__ == "__main__":
    create_pin_1()
