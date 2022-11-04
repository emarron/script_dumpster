OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.*" -type f)
    do
    opacity=$(magick identify -format '%[opaque]' $file)
    width=$(magick identify -format '%w' $file)
    height=$(magick identify -format '%h' $file)
    output=${file#$1}
    if [ $width -ge 8192 ] || [ $height -ge 8192 ]
    then
        echo "neat"
    else
        if [ $opacity == 'True' ]
        then
            echo "opacity (RGB) is true, d<8192, saving as BC7" 
            ./cuttlefish.exe -i $file -j -m -f BC7  -Q highest -o "dds/${output%.*}.dds" --create-dir             
        fi
    fi
done   
IFS="$OIFS"