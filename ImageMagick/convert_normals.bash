# command: `bash convertnormals.txt input.png output.png`, converts most common object normal map to skyrim standard.
for file in *.png; do
	convert $file -channel B -negate - | convert - -separate -swap 0,2 -combine ${file%.png}_out.png
done