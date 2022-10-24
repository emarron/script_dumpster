OIFS="$IFS"
IFS=$'\n'
for file in $(find $1 -name "*.tga" -type f)
do
    output=${file#$1}
    echo $output
    echo "outputting BC3, highest quality"
    ./cuttlefish.exe -i $file -j -m -f BC3  -Q highest -o "dds/highest/${output%.tga}.dds" --create-dir
    echo "outputting BC3, high quality"
    ./cuttlefish.exe -i $file -j -m -f BC3  -Q high -o "dds/high/${output%.tga}.dds" --create-dir
    echo "outputting BC3, normal quality"
        ./cuttlefish.exe -i $file -j -m -f BC3  -Q normal -o "dds/normal/${output%.tga}.dds" --create-dir
    echo "outputting BC3, low quality"
        ./cuttlefish.exe -i $file -j -m -f BC3  -Q low -o "dds/low/${output%.tga}.dds" --create-dir
    echo "outputting BC3, lowest quality"
        ./cuttlefish.exe -i $file -j -m -f BC3  -Q lowest -o "dds/lowest/${output%.tga}.dds" --create-dir   
done   
IFS="$OIFS"