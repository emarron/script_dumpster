OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name "*.dds") 
    do magick convert "$file" "${file%.dds}.png"
	done
IFS="$OIFS"