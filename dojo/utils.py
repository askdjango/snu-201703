import os
from django.conf import settings
from django.utils.six import BytesIO
from PIL import Image, ImageDraw, ImageFont


def get_nametag_file(name):
    with Image.new('RGB', (256, 256), 'blue') as canvas:
        font = ImageFont.truetype(os.path.join(settings.BASE_DIR, "D2Coding.ttf"), 24)
        text_width, text_height = font.getsize(name)
        x = (canvas.width - text_width) // 2
        y = (canvas.height - text_height) // 2

        draw = ImageDraw.Draw(canvas)
        draw.text((x, y), name, font=font)

        io = BytesIO()
        canvas.save(io, format='PNG')
        io.seek(0)

        return io

