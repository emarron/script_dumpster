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


def image_path(folder_path, file_path):
    string = str(folder_path) + '/' + '/'.join(file_path.parts[1:-1]) + '/' + str(file_path.stem) + '.png'
    return string


def save(output_folder, file_path, created_image):
    try:
        created_image.save(str(output_folder) + '/' + '/'.join(file_path.parts[1:-1]) + '/' + str(file_path.stem) + '.' + sys.argv[3])
    except IndexError:
        created_image.save(str(output_folder) + '/' + '/'.join(file_path.parts[1:-1]) + '/' + str(file_path.stem) + '.' + 'tga')


# sys.agrv is the folder selected
folder = sys.argv[1]
images = check_path('./' + folder)
extensions = ['png', 'tga', 'jpg', 'dds']
ignore_list = shutil.ignore_patterns(*['*.' + extension for extension in extensions])
globs = [list(images.glob(f'**/*.{extension}')) for extension in extensions]
global_count = sum(len(glob) for glob in globs)

if sys.argv[2] == 'split':
    images_rgb = check_path('./' + folder + '_rgb')
    images_alpha = check_path('./' + folder + '_alpha')
    copy_tree(images, images_alpha)
    copy_tree(images, images_rgb)
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        try:
            image = Image.open(file)
            image.convert('RGB').save(image_path(images_rgb, file))
            try:
                alpha = image.getchannel('A')
                alpha.save(image_path(images_alpha, file))
            except ValueError:
                pass
        except ValueError:
            pass
if sys.argv[2] == 'merge':
    images_rgb = check_path('./' + folder + '_rgb')
    images_alpha = check_path('./' + folder + '_alpha')
    images_merged = check_path('./' + folder + '_merged')
    copy_tree(images, images_merged)
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        try:
            alpha = Image.open(image_path(images_alpha, file))
            alpha = ImageOps.grayscale(alpha)
            image = Image.open(file)
            out = Image.new("RGBA", image.size, (255, 255, 255, 255))
            out.paste(image)
            out.putalpha(alpha)
        except FileNotFoundError:
            out = Image.open(file)
        save(images_merged, file, out)
if sys.argv[2] == '4split':
    images_alpha = check_path('./' + folder + '_alpha')
    images_red = check_path('./' + folder + '_red')
    images_green = check_path('./' + folder + '_green')
    images_blue = check_path('./' + folder + '_blue')
    copy_tree(images, images_alpha)
    copy_tree(images, images_red)
    copy_tree(images, images_green)
    copy_tree(images, images_blue)
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        try:
            image = Image.open(file)
            red = image.getchannel('R')
            green = image.getchannel('G')
            blue = image.getchannel('B')
            red.save(str(images_red) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.png')
            green.save(str(images_green) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.png')
            blue.save(str(images_blue) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.png')

            try:
                alpha = image.getchannel('A')
                alpha.save(str(images_alpha) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.png')
            except ValueError:
                pass
        except ValueError:
            pass
if sys.argv[2] == '4merge':
    images_alpha = check_path('./' + folder + '_alpha')
    images_red = check_path('./' + folder + '_red')
    images_green = check_path('./' + folder + '_green')
    images_blue = check_path('./' + folder + '_blue')
    images_merged = check_path('./' + folder + '_merged')
    copy_tree(images, images_merged)
    local_count = 0
    for file in itertools.chain.from_iterable(globs):
        local_count = local_count + 1
        print("Processing " + file.stem + " File: " + str(local_count) + "/" + str(global_count))
        try:
            r = Image.open(image_path(images_red, file)).convert('L')
            g = Image.open(image_path(images_green, file)).convert('L')
            print("bonk")
            b = Image.open(image_path(images_blue, file)).convert('L')
            print(file)
            try:
                alpha = Image.open(image_path(images_alpha, file))
                alpha = ImageOps.grayscale(alpha)
                out = Image.merge('RGBA', (r, g, b, alpha))
            except FileNotFoundError:
                out = Image.merge('RGB', (r, g, b))
        except FileNotFoundError:
            out = None
        save(images_merged, file, out)
