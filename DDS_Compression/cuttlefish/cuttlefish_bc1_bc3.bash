OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.tga" -type f)
    do var1=$(magick identify -format '%[opaque]' $file)
    if [ $var1 == 'True' ]
        then ./cuttlefish.exe -i $file -j -m -f BC1  -Q highest -o "dds/${file%.tga}.dds" --create-dir
    else ./cuttlefish.exe -i $file -j -m -f BC3 -Q highest -o "dds/${file%.tga}.dds" --create-dir
    fi
done   
IFS="$OIFS"