import excel2img
from PIL import Image


def excel2image(filename: str, output_path: str, sheet_name: str, cell_area: str, crop_edge: bool = True) -> None:
    excel2img.export_img(filename, output_path, sheet_name, cell_area)
    if crop_edge:
        im = Image.open(output_path)
        width, height = im.size
        left = 1
        top = 1
        right = width - 1
        bottom = height - 1
        im_crop = im.crop(left, top, right, bottom)
        im_crop.save(output_path)
