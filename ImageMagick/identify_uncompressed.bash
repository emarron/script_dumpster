OIFS="$IFS"
IFS=$'\n'
for i in $(find * -type f)
do 
	magick identify -verbose "$i" | grep -q 'Compression: None' && echo $i
done
IFS="$OIFS"