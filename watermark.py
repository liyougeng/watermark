#!/usr/bin/env python
#!-coding:utf-8
""" A SIMPLE SCRIPT TO GENERATE THE TEXT_WATERMARK FOR IMAGES
   usage: python watermark.py img_path_in img_path_out text
"""
from PIL import Image, ImageDraw, ImageFont
def watermark(jpg_in, jpg_out, text, text_angle=30, spacing_w=50, spacing_h=50, font_size=24, alpha=48):
    base = Image.open(jpg_in).convert('RGBA')
    base_w, base_h = base.size
    max_base_edge = max(base_w, base_h) * 2
    txt = Image.new('RGBA', (max_base_edge, max_base_edge), (255,255,255,0))
    # or use font: https://github.com/jingle1267/watermark/raw/master/fzhtjt.ttf
    fnt = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', font_size, encoding="unic")
    d = ImageDraw.Draw(txt)
    txt_w, txt_h = d.textsize(text.decode('utf-8'), font=fnt)
    for x in xrange(0, txt.size[0], txt_w+spacing_w):
        line_cc = 0
        for y in xrange(0, txt.size[1], txt_h+spacing_h):
            line_cc += 1
            d.text((x - ((line_cc * txt_w / 3) % txt_w), y), text.decode('utf-8'), font=fnt, fill=(255,255,255,alpha))
    txt = txt.rotate(text_angle)
    crop_left, crop_top = (max_base_edge - base_w) / 2, (max_base_edge - base_h) / 2
    crop_right, crop_lower = crop_left + base_w, crop_top + base_h
    txt = txt.crop((crop_left, crop_top, crop_right, crop_lower))
    out = Image.alpha_composite(base, txt)
    out.show()
    out = out.convert('RGB')
    out.save(jpg_out)

if __name__ == "__main__":
    watermark(sys.argv[1], sys.argv[2], sys.argv[3])
