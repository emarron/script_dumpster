OIFS="$IFS"
IFS=$'\n'
for i in $(find $1 -type f -name '*.dds')
do 
	magick identify -verbose "$i" | grep -q 'Compression: None' && echo $i
done
IFS="$OIFS"