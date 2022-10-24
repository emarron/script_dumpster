OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.tga" -type f) 
    do ./cuttlefish.exe -i $file -j -m -f BC7  -Q highest -o "dds/${file%.tga}.dds" --create-dir
    done   
IFS="$OIFS"