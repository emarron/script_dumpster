OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2)
    do var1=$(magick identify -format '%[opaque]' $file)
    if [ $var1 == 'False' ]
        then echo $var1
        fi
    done  
IFS="$OIFS"