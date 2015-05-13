A script to sort contents of an Ipod so they can be understood by humans and store the result in a folder.

The package TinyTag is used in this script, so you have to install it (if you don't already have it) before you run the script.

To run the script you need to type:

python3 ipodhack.py "path/to/folder/being/sorted" "path/to/the/folder/containing/the/result"

The resulting folder will contain a folder for all artists containing subfolders (albums by each artist) which then contain the songs of each album.

Songs with no title or album name are given the title/album name: "Untitled".
