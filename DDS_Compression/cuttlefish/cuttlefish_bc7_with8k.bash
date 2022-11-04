OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.*" -type f)
    do
    width=$(magick identify -format '%w' $file)
    height=$(magick identify -format '%h' $file)
    output=${file#$1}
    if [ $width -ge 8192 ] || [ $height -ge 8192 ]
    then
        echo "d>=8192, saving as BC7, 12mipmaps" 
        ./cuttlefish.exe -i $file -j -m 12 -f BC7  -Q highest -o "dds/${output%.*}.dds" --create-dir
    else 
        echo "d<8192, saving as BC7"  
        ./cuttlefish.exe -i $file -j -m -f BC7  -Q highest -o "dds/${output%.*}.dds" --create-dir
    fi

done   
IFS="$OIFS"