import argparse
import csv
import gensim.downloader as api
import sys
from tabulate import tabulate

# This script allows the user to select any word and generate a list of "good neighbors".
# Good neighbors of a word are, among the 500 nearest neighbors to that word in a Word2Vec 
# vector space, those items that also have the original word as one of their nearest neighbors.
# Currently the original word must be one of the 25 closest neighbors of a potential
# good neighbor to qualify; later versions of the script will allow the user to set that
# threshold at runtime.

parser = argparse.ArgumentParser(
	description='Generate a list of near neighbors for a given word.'
)
parser.add_argument('word', help='The word to look up')
parser.add_argument(
	'-w', '--words-only',
	help='Return only words, not their distances',
	action='store_true'
	)
parser.add_argument(
	'-t', '--tables',
	help='Print results in table form',
	action='store_true'
	)
args = parser.parse_args()

model = api.load("glove-wiki-gigaword-300")
	
similar = model.similar_by_word(args.word, topn=500)

good_neighbors = []

for i in similar:
	word_dist = i[1]
	neighbor = i[0]
	n_similar = model.similar_by_word(neighbor, topn=25)
	most_distant = n_similar[-1]
	if most_distant[1] <= word_dist:
		if args.words_only:
			good_neighbors.append((i[0],))
		else:
			good_neighbors.append(i)
		
if args.tables:
	print(tabulate(good_neighbors))
else:
	csvwriter = csv.writer(sys.stdout)
	for row in good_neighbors:
		csvwriter.writerow(row)