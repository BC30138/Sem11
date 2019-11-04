"""Main code here"""
import io

from PIL import Image

def resize(request):
    """
    IGOR NIKOLAEV WAITING
    """
    size = (512, 256)
    image = Image.open(request.files['image'])
    image = image.resize(size)
    with io.BytesIO() as output:
        image.save(output, format="JPEG")
        contents = output.getvalue()
    return contents
