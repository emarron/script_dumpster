import itertools
import shutil
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageChops

Image.MAX_IMAGE_PIXELS = None


def check_path(path):
    if not Path(path).exists():
        Path(path).mkdir()
    return Path(path)


def copy_tree(source, destination):
    shutil.rmtree(destination)
    shutil.copytree(source, destination, ignore=ignore_list)


def flat_image_path(file_stem, file_parent):
    string = str(file_parent).replace('\\', '') + str(file_stem)
    return string


def save(output_folder, file_path, created_image):
    try:
        created_image.save(
            str(output_folder) + '/' + '/'.join(file_path.parts[1:-1]) + '/' + str(file_path.stem) + '.' + sys.argv[3])
    except IndexError:
        created_image.save(
            str(output_folder) + '/' + '/'.join(file_path.parts[1:-1]) + '/' + str(file_path.stem) + '.tga')


# sys.agrv is the folder selected
if sys.argv[1].endswith("/") or sys.argv[1].endswith("\\"):
    folder = sys.argv[1][:-1]
else:
    folder = sys.argv[1]
images = check_path('./' + folder)
extensions = ['png', 'tga', 'jpg', 'dds']
ignore_list = shutil.ignore_patterns(*['*.' + extension for extension in extensions])
globs = [list(images.glob(f'**/*.{extension}')) for extension in extensions]
global_count = sum(len(glob) for glob in globs)

if sys.argv[2] == 'flatten':
    images_rgb = check_path('./' + folder + '_flat_rgba')
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        flattened_path = flat_image_path(file.stem, file.parent)
        try:
            image = Image.open(file)
            image.convert('RGBA').save(str(images_rgb) + "//" + flattened_path + '.png')
        except ValueError:
            pass
if sys.argv[2] == 'unflatten':
    images_rgb = check_path('./' + folder + '_flat_rgba')
    images_merged = check_path('./' + folder + '_merged')
    copy_tree(images, images_merged)
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        flattened_path = flat_image_path(file.stem, file.parent)
        try:
            RGB = Image.open(str(images_rgb) + '//' + flattened_path + '.png')
            out = RGB
            save(images_merged, file, out)
        except FileNotFoundError:
            pass
