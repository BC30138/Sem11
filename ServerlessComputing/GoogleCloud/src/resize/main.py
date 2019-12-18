"""Main code here"""
from io import BytesIO
import zipfile
import base64
from PIL import Image

def resize(request):
    """
    IGOR NIKOLAEV WAITING
    """
    sizes = [(512, 256), (256, 512)]
    image = Image.open(BytesIO(base64.b64decode(request.data)))
    memory_zip = BytesIO()
    with zipfile.ZipFile(memory_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
        for size in sizes:
            buffered = BytesIO()
            image.resize(size).save(buffered, format="JPEG")
            filename = str(size[0]) + "x" + str(size[1]) + ".jpeg"
            zf.writestr(filename, buffered.getvalue())
    return base64.b64encode(memory_zip.getvalue())
