"""Main code here"""
from io import BytesIO
import base64
from flask import jsonify

from PIL import Image

def resize(request):
    """
    IGOR NIKOLAEV WAITING
    """
    sizes = [(512, 256), (256, 512)]
    image = Image.open(request.files['image'])
    result = {}
    result['resized_images'] = []
    for size in sizes:
        buffered = BytesIO()
        image.resize(size).save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        result['resized_images'].append(img_str)

    return jsonify(result)
