import itertools
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageOps


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
folder = sys.argv[1]
images = check_path('./' + folder)
extensions = ['png', 'tga', 'jpg', 'dds']
ignore_list = shutil.ignore_patterns(*['*.' + extension for extension in extensions])
globs = [list(images.glob(f'**/*.{extension}')) for extension in extensions]
global_count = sum(len(glob) for glob in globs)

if sys.argv[2] == 'split':
    images_rgb = check_path('./' + folder + '_flat_rgb')
    images_alpha = check_path('./' + folder + '_flat_alpha')
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        flattened_path = flat_image_path(file.stem, file.parent)
        try:
            image = Image.open(file)
            image.convert('RGB').save(str(images_rgb) + "//" + file.stem + '.png')
            try:
                alpha = image.getchannel('A')
                alpha.save(str(images_alpha) + "//" + file.stem + '.png')
            except ValueError:
                pass
        except ValueError:
            pass
if sys.argv[2] == 'merge':
    images_rgb = check_path('./' + folder + '_flat_rgb')
    images_alpha = check_path('./' + folder + '_flat_alpha')
    images_merged = check_path('./' + folder + '_merged')
    copy_tree(images, images_merged)
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        flattened_path = flat_image_path(file.stem, file.parent)
        try:

            RGB = Image.open(str(images_rgb) + '//' + file.stem + '.png')
            try:
                alpha = Image.open(str(images_alpha) + '//' + file.stem + '.png')
                alpha = ImageOps.grayscale(alpha)
                out = Image.new("RGBA", RGB.size, (255, 255, 255, 255))
                out.paste(RGB)
                out.putalpha(alpha)
            except FileNotFoundError:
                out = RGB
            save(images_merged, file, out)
        except FileNotFoundError:
            pass

if sys.argv[2] == '4split':
    images_alpha = check_path('./' + folder + '_flat_alpha')
    images_red = check_path('./' + folder + '_flat_red')
    images_green = check_path('./' + folder + '_flat_green')
    images_blue = check_path('./' + folder + '_flat_blue')
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        flattened_path = flat_image_path(file.stem, file.parent)
        try:
            image = Image.open(file)
            red = image.getchannel('R')
            green = image.getchannel('G')
            blue = image.getchannel('B')
            red.save(str(images_red) + "//" + file.stem + '.png')
            green.save(str(images_green) + "//" + file.stem + '.png')
            blue.save(str(images_blue) + "//" + file.stem + '.png')
            try:
                alpha = image.getchannel('A')
                alpha.save(str(images_alpha) + "//" + file.stem + '.png')
            except ValueError:
                pass
        except ValueError:
            pass

if sys.argv[2] == '4merge':
    images_alpha = check_path('./' + folder + '_flat_alpha')
    images_red = check_path('./' + folder + '_flat_red')
    images_green = check_path('./' + folder + '_flat_green')
    images_blue = check_path('./' + folder + '_flat_blue')
    images_merged = check_path('./' + folder + '_flat_merged')
    local_count = 0
    copy_tree(images, images_merged)
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        flattened_path = flat_image_path(file.stem, file.parent)
        try:
            r = Image.open(str(images_red) + '//' + file.stem + '.png').convert('L')
            g = Image.open(str(images_green) + '//' + file.stem + '.png').convert('L')
            b = Image.open(str(images_blue) + '//' + file.stem + '.png').convert('L')
            try:
                alpha = Image.open(str(images_alpha) + '//' + file.stem + '.png').convert('L')
                out = Image.merge('RGBA', (r, g, b, alpha))
            except FileNotFoundError:
                out = Image.merge('RGB', (r, g, b))
        except FileNotFoundError:
            out = None
        save(images_merged, file, out)
