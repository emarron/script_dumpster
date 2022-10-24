OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2) 
    do var1=$(magick identify -format '%[opaque]' $file)
    echo $var1
    if [ $var1 == 'True' ]
        then ./nvtt_export.exe $file -f 15 --no-mip-pre-alpha --quality 1
    else ./nvtt_export.exe $file -f 18 --no-mip-pre-alpha --quality 1
    fi
done   
IFS="$OIFS"