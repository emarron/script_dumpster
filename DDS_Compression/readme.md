## Recursive DDS compression/conversion.

 Not super fast, but gets the job done.
 
Requires [NVidia Texture Tools Standalone](https://developer.nvidia.com/nvidia-texture-tools-exporter) to be in the same folder as scripts (or the folder the command is being executed.)


# BASH SCRIPTS:

- nvidiacompress_BC1.bash - converts files to BC1 DDS with the "good" compression method.
- nvidiacompress_BC1_BC3.bash - converts RGB files to BC1 DDS or RGBA files to BC3 DDS with the "good" compression method.
- nvidiacompress_RGBA_uncompressed.bash converts only RGBA files to BGRA uncompressed DDS.
- nvidiacompress_uncompressed.bash - converts files to BGRA uncompressed dds.

**USAGE:**

    bash file.bash folder 'reg_ex name search'

folder = your folder, e.g. cat

reg_ex name search = name of files you want to process, e.g. '*_d.tga' would process all files that end in "_d.tga"

**EXAMPLE:**

     bash nvidiacompress_BC1.bash images_upscaled '*_d.png'

## WINDOWS BAT:

- DDS_compressor.bat

**USAGE:**
DDS_compressor.bat folder 'reg_ex name search' compression

folder = folder to process

reg_ex name search = name of files you want to process, e.g. '*_d.tga' would process all files that end in "_d.tga"

compression = NVidia Texture Tools Exporter Standalone compression number. From docs:

>   -f,--format
> INT:{a8->0,astc-ldr-10x10->1,astc-ldr-10x5->2,astc-ldr-10x6->3,astc-ldr-10x8->4,astc-ldr-12x10->5,astc-ldr-12x12->6,astc-ldr-4x4->7,astc-ldr-5x4->8,astc-ldr-5x5->9,astc-ldr-6x5->10,astc-ldr-6x6->11,astc-ldr-8x5->12,astc-ldr-8x6->13,astc-ldr-8x8->14,bc1->15,bc1a->16,bc2->17,bc3->18,bc3n->19,bc4->20,bc5->21,bc6->22,bc7->23,bgr8->24,bgra8->25,bgrx8->26,l8->27,r16f->28,r32f->29,rg16f->30,rg32f->31,rgba16f->32,rgba32f->33}
>                               When converting to DDS, the DXGI format to convert to (default: bc7). For most RGBA images, try using BC7. For
> three-channel HDR images, try using BC6H. BC4 and BC5 are good for
> one-channel (red) and two-channel (red, green) images, respectively.
> ASTC images will be stored uncompressed on many desktop GPUs, but are
> good for non-HDR RGBA images on Tegra GPUs.

**EXAMPLE:**

    DDS_compressor.bat dogs_upscaled '*.png' 23

Compresses all images in dogs_upscaled that were PNG files to BC7 DDS.
