OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2) 
    do ./nvtt_export.exe $file -f 15 --no-mip-pre-alpha --quality 1
    done   
IFS="$OIFS"