OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.png" -type f)
    do
    opacity=$(magick identify -format '%[opaque]' $file)
    width=$(magick identify -format '%w' $file)
    height=$(magick identify -format '%h' $file)
    output=${file#$1}
    if [ $width -ge 8192 ] || [ $height -ge 8192 ]
    then
        if [ $opacity == 'True' ]
        then
            echo "opacity (RGB) is true, d>=8192, saving as BC7, 12mipmaps" 
            ./cuttlefish.exe -i $file -j -m 12 -f BC7  -Q highest -o "dds/${output%.png}.dds" --create-dir
        else 
            echo "opacity (RGBA) is false, d>=8192, saving as BC3, 12mipmaps" 
            ./cuttlefish.exe -i $file -j -m 12 -f BC3 -Q normal -o "dds/${output%.png}.dds" --create-dir
        fi
    else
        if [ $opacity == 'True' ]
        then
            echo "opacity (RGB) is true, d<8192, saving as BC7" 
            ./cuttlefish.exe -i $file -j -m -f BC3  -Q highest -o "dds/${output%.png}.dds" --create-dir
        else
            if [ $width -le 512 ] || [ $height -le 512 ]
            then
                echo "opacity (RGBA) is false, d<=512, saving as BGRA" 
                ./cuttlefish.exe -i $file -j -m -f B8G8R8A8 -o "dds/${output%.png}.dds" --create-dir
            else
                echo "opacity (RGBA) is false, 512<d<8192, saving as BC3" 
                ./cuttlefish.exe -i $file -j -m -f BC3 -Q normal -o "dds/${output%.png}.dds" --create-dir
            fi               
        fi
    fi
done   
IFS="$OIFS"