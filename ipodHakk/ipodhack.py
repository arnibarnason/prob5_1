from tinytag import TinyTag as t
import os
import argparse
from urllib.parse import quote

parser = argparse.ArgumentParser(description="""Takes a path to a folder as first parameter and finds info on the songs within and sorts them into the folder contained in the path of the second parameter""")
parser.add_argument('source', help='Path to the folder being sorted')
parser.add_argument('target', help='Path to the folder containing the result')
args = parser.parse_args()

for root, dirs, files in os.walk(args.source):
	for g in files:
            tag = t.get(os.path.join(os.path.abspath(root), g))
            if tag.title is None:
                tag.title = 'Untitled'
            else:
                title = tag.title.strip(' \t\r\n\0').replace('/', '-')
            if tag.album is None:
                tag.album = 'Untitled'
            if not tag.artist is None:
                path = os.path.join(args.target, 
                        tag.artist.strip(' \t\r\n\0').replace('/', '-'), 
                        tag.album.strip(' \t\r\n\0').replace('/', '-'))                
                if not os.path.exists(path):
                    os.makedirs(path)
                os.rename(os.path.join(os.path.abspath(root),g), os.path.join(path, title))
            else:
                path = os.path.join(args.target, title)
                if not os.path.exists(path):
                    os.makedirs(path)
                os.rename(os.path.join(os.path.abspath(root),g), 
                        os.path.join(path, title))

