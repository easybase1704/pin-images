# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os
D = r'C:\Users\rb\pin-images\week11'
TW,TH = 330,495
f = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 34)
sheet = Image.new('RGB',(TW*4, TH*2),(255,255,255)); d = ImageDraw.Draw(sheet)
for k in range(7):
    p = os.path.join(D, f'week11-0{k+1}.jpg')
    im = Image.open(p).convert('RGB').resize((TW,TH), Image.LANCZOS)
    x,y = (k%4)*TW, (k//4)*TH
    sheet.paste(im,(x,y)); d.rectangle([x,y,x+64,y+42], fill=(0,0,0)); d.text((x+10,y+4),str(k+1),font=f,fill=(255,255,255))
out = os.path.join(D,'_week11covers.jpg'); sheet.save(out,'JPEG',quality=90); print(out)
