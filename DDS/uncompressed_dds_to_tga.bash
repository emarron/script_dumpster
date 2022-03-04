OIFS="$IFS"
IFS=$'\n'
for file in $(find * -type f); do .././nvtt_export.exe $file -o ${file%.dds}.tga ; done  
IFS="$OIFS"