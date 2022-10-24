OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2) 
    do ./nvtt_export.exe $file -f 23 -q 2
    done   
IFS="$OIFS"