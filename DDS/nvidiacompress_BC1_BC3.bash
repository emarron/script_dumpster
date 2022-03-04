OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f) 
    do var1=$(magick identify -format '%[opaque]' $file)
    echo $var1
    if [ $var1 == 'True' ]
        then ./nvtt_export.exe $file -f 15
        else ./nvtt_export.exe $file -f 18
        fi
    done   
IFS="$OIFS"