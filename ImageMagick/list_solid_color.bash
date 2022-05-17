OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2) 
    do var1=$(magick identify -format %k $file)
    if [ $var1 == 1 ]
        then echo $file
    fi
    done   
IFS="$OIFS"