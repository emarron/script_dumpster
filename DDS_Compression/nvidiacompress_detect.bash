OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2) 
    do var1=$(magick identify -format '%[compression]' $file)
    echo $file $var1
    if [ $var1 == 'DXT1' ]
        then ./nvtt_export.exe $file -f 15 --no-mip-pre-alpha --quality 1 -o  $file.out
    if [ $var1 == 'DXT5' ]
        then ./nvtt_export.exe $file -f 18 --no-mip-pre-alpha --quality 1 -o $file.out
    else ./nvtt_export.exe $file -f 25 --no-mip-pre-alpha -o $file.out
    fi
done   
IFS="$OIFS"