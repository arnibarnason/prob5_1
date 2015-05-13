from tinytag import TinyTag as t
import os
import argparse

parser = argparse.ArgumentParser(description="""Takes a path to a folder as first parameter and finds info on the songs within and sorts them into the folder contained in the path of the second parameter""")
parser.add_argument('source', help='Path to the folder being sorted')
parser.add_argument('target', help='Path to the folder containing the result')
args = parser.parse_args()

for root, dirs, files in os.walk(args.source):
	for g in files:
            #print(g)


