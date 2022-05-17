## flattener and splitters.

Requires Python 3, [Python Pillow Library](https://pillow.readthedocs.io/en/stable/installation.html)

**Why?**

 - Many programs screw with image channels in unwanted ways.
 - Many programs don't support my usual image filetypes (TGA, DDS.) 
 - Many programs don't support nested directory structures.

So I have "flattener" which flattens a nested directory for processing, and "splitter" which splits an image into different channel configurations for processing. I have also combined the two, which is what I most commonly use.

**Is there a better way to do this?**
Yeah, probably, I mean I could structure this better and use C++ to make it faster, but well, "it just works."

## flattener.py:

Given nested directory structure of images *nest*, flattener will convert it to PNG file type, and flatten it to *nest_flat_rgba*. Program uses *nest* directory to later unflatten *nest_rgba*. By default outputs merged result as TGA.
**USAGE:** 
given: folder/cat/dog/apple.png

command: `python flattener.py folder flatten`

result: folder_flat/foldercatdogapple.png

given: folder/cat/dog/apple.png AND folder_flat/foldercatdogapple.png

command: `python flattener.py folder unflatten png`

result: folder_merged/cat/dog/apple.png

## splitter.py:

Given nested directory structure of images *nest*, splitter will split into *nest_rgb* and *nest_alpha*, or *nest_red*, *nest_green*, *nest_blue*, and *nest_alpha* channels. Program uses *nest* directory to later merge *nest* channels. By default outputs merged result as TGA.

**USAGE:**

**RGB and alpha split**
given: folder/cat/dog/apple.dds

command: `python splitter.py folder split`

result: folder_rgb/cat/dog/apple.png AND folder_alpha/cat/dog/apple.png (if alpha exists)

given: folder/cat/dog/apple.dds AND folder_rgb/cat/dog/apple.png AND folder_alpha/cat/dog/apple.png (if alpha exists)

command: `python splitter.py folder merge`

result: folder_merged/cat/dog/apple.tga

**Red, green, blue, and alpha split**
given: folder/cat/dog/apple.dds

command: `python splitter.py folder 4split`

result: folder_red/cat/dog/apple.png AND folder_green/cat/dog/apple.png AND folder_blue/cat/dog/apple.png AND folder_alpha/cat/dog/apple.png (if alpha exists)

given: folder/cat/dog/apple.dds AND folder_red/cat/dog/apple.png AND folder_green/cat/dog/apple.png AND folder_blue/cat/dog/apple.png AND folder_alpha/cat/dog/apple.png (if alpha exists)

command: `python splitter.py folder 4merge`

result: folder_merged/cat/dog/apple.tga

## splitter_flattener.py:

Does the same thing as splitter.py and flattener.py in one script.

**USAGE:**
**RGB and alpha split**
given: folder/cat/dog/apple.dds

command: `python splitter_flattener.py folder split`

result: folder_rgb/foldercatdogapple.png AND folder_alpha/foldercatdogapple.png (if alpha exists)

given: folder/cat/dog/apple.dds AND folder_rgb/foldercatdogapple.png AND folder_alpha/foldercatdogapple.png (if alpha exists)
command: `python splitter.py folder merge`

result: folder_merged/cat/dog/apple.tga

given: folder/cat/dog/apple.png

**Red, green, blue, and alpha split**

command: `python splitter.py folder 4split`

command: `python splitter.py folder 4merge`

result: folder_merged/cat/dog/apple.png

## splitter_pathless_flattener.py:

Does the same thing as splitter_flattener.py, except only the name is preserved not the path.

**USAGE:**
**RGB and alpha split**

given: folder/cat/dog/apple.dds

command: `python splitter_pathless_flattener.py folder split`

result: folder_rgb/apple.png AND folder_alpha/apple.png (if alpha exists)

given: folder/cat/dog/apple.dds AND folder_rgb/apple.png AND folder_alpha/apple.png (if alpha exists)

command: `python splitter_pathless_flattener.py folder merge`

result: folder_merged/cat/dog/apple.tga

**Red, green, blue, and alpha split**
command: `python splitter_pathless_flattener.py folder 4split`

command: `python splitter_pathless_flattener.py folder 4merge`
result: folder_merged/cat/dog/apple.png
