OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type $2) 
    do var1=$(magick identify -format '%[opaque]' $file)
    echo $var1
    if [ $var1 != 'True' ]
        then ./nvtt_export.exe $file -f 25 --no-mip-pre-alpha
        fi
    done   
IFS="$OIFS"