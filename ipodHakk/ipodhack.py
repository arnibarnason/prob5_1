from tinytag import TinyTag as t
import os
import argparse
from urllib.parse import quote

# Handle arguments
parser = argparse.ArgumentParser(description="""Takes a path to a folder as first parameter and finds info on the songs within and sorts them into the folder contained in the path of the second parameter""")
parser.add_argument('source', help='Path to the folder being sorted')
parser.add_argument('target', help='Path to the folder containing the result')
args = parser.parse_args()

# Counter of untitled songs
count = 0
# Loop through all the files in the source folder
for root, dirs, files in os.walk(args.source):
	for g in files:
            # Use tinytag to get metadata from songs
            tag = t.get(os.path.join(os.path.abspath(root), g))
            # If the metadata has no name for album, title or artist we give the name 'Untitled'
            if tag.title is None:
                title = 'Untitled' + str(count)
                count += 1
            else:
                title = tag.title.strip(' \t\r\n\0').replace('/', '-')
            if tag.album is None:
                tag.album = 'Untitled'
            if not tag.artist is None:
                # Path contains the path of the target folder for the current song
                path = os.path.join(args.target, 
                        tag.artist.strip(' \t\r\n\0').replace('/', '-'), 
                        tag.album.strip(' \t\r\n\0').replace('/', '-'))
                # Create the folder structure for file if it hasn't been created already
                if not os.path.exists(path):
                    os.makedirs(path)
                # Move and rename the song to the correct folder
                os.rename(os.path.join(os.path.abspath(root),g), os.path.join(path, title))
            else:
                # Path of the target folder of the untitled artist
                path = os.path.join(args.target, title)
                # Create folder structure
                if not os.path.exists(path):
                    os.makedirs(path)
                # Move and rename song
                os.rename(os.path.join(os.path.abspath(root),g), 
                        os.path.join(path, title))
