OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.*" -type f)
    do var1=$(magick identify -format '%[opaque]' $file)
    if [ $var1 == 'True' ]
        then ./cuttlefish.exe -i $file -j -m -f BC7  -Q highest -o "dds/${file%.*}.dds" --create-dir
    else ./cuttlefish.exe -i $file -j -m -f B8G8R8A8 -o "dds/${file%.*}.dds" --create-dir
    fi
done   
IFS="$OIFS"