OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -type f -name $2)
do
	magick identify -format '%[channels]' $file | grep 'rgba' && echo $file
done
IFS="$OIFS"
