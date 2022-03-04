OIFS="$IFS"
IFS=$'\n'
for file in $(find * -type f)
do
	magick identify -format '%[channels]' $file | grep 'rgba' && echo $file
done
IFS="$OIFS"
