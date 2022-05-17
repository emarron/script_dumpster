
#Format: python movewithstructure.py list-of-files-to-move.txt output_folder
import shutil
import sys
from pathlib import Path

try:
    txtfile = sys.argv[1]
except IndexError:
    print("Please pick a textfile to read.")
    sys.exit()
try:
    target = sys.argv[2]
except IndexError:

    print("No directory given, using './badfiles'.")
    target = "./bad_files"

target_path = Path(target)
if target_path.exists():
    shutil.rmtree(target_path)
target_path.mkdir()

with Path(sys.argv[1]).open('r') as f:
    for line in f:
        line = line.strip()
        source = Path(line)
        destination = target_path / source.relative_to('.')
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(source, destination)
