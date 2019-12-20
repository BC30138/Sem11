"""Main code here"""
from io import BytesIO
import zipfile
import base64
from PIL import Image

def image_processing(image: Image.Image,
                     size: tuple, os_str: str) -> tuple:
    """image resizing and response-preprocessing"""
    buffered = BytesIO()
    image.resize(size).save(buffered, format="PNG")
    filename = os_str + "/icon_" + str(size[0]) + "x" + str(size[1]) + ".png"
    return filename, buffered.getvalue()

def resize(request):
    """
    Endpoint main function
    """
    ios_sizes = [(16, 16), (20, 20), (29, 29), (32, 32),
                 (40, 40), (48, 48), (50, 50), (55, 55),
                 (57, 57), (58, 58), (60, 60), (64, 64),
                 (72, 72), (76, 76), (80, 80), (87, 87),
                 (88, 88), (100, 100), (114, 114), (120, 120),
                 (128, 128), (144, 144), (152, 152), (167, 167),
                 (172, 172), (180, 180), (196, 196), (256, 256),
                 (512, 512), (1024, 1024)]
    android_sizes = [(36, 36), (48, 48), (72, 72), (96, 96),
                     (144, 144), (192, 192), (512, 512)]
    watch_sizes = [(48, 48), (55, 55), (80, 80), (88, 88),
                   (172, 172), (196, 196)]
    image = Image.open(BytesIO(base64.b64decode(request.data)))
    memory_zip = BytesIO()
    with zipfile.ZipFile(memory_zip, mode="w",
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for size in ios_sizes:
            filename, base64_resized = image_processing(image, size, 'ios')
            zf.writestr(filename, base64_resized)
        for size in android_sizes:
            filename, base64_resized = image_processing(image, size, 'android')
            zf.writestr(filename, base64_resized)
        for size in watch_sizes:
            filename, base64_resized = image_processing(image, size, 'watch')
            zf.writestr(filename, base64_resized)
    return base64.b64encode(memory_zip.getvalue())
