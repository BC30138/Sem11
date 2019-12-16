"""Main code here"""
import io
from flask import jsonify

from PIL import Image

def resize(request):
    """
    IGOR NIKOLAEV WAITING
    """
    request_json = request.get_json(silent=True)

    # size = (512, 256)
    # image = Image.open(request.files['image'])
    # image = image.resize(size)
    result = {'result': request_json['name']}

    # with io.BytesIO() as output:
    # image.save(output, format="JPEG")
        # contents = output.getvalue()
    return jsonify(result)
