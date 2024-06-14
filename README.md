This script allows the user to select any word and generate a list of "good neighbors". Good neighbors of a word are, among the 500 nearest neighbors to that word in a Word2Vec vector space, those items that also have the original word as one of their nearest neighbors. Currently the original word must be one of the 25 closest neighbors of a potential good neighbor to qualify. (Later versions of the script will allow the user to set that threshold at runtime.) 

This script uses the glove-wiki-gigaword-300 pre-trained model as its reference vector space. For more information about this model and others like it, see: https://github.com/RaRe-Technologies/gensim-data

## Setup and usage: Mac OS

1. Check out the code from Github: In the terminal, navigate to the directory where you want to save and run the code, then enter `git clone https://github.com/vtobin/goodneighbors.git`
2. Navigate to the directory you've just installed: `cd goodneighbors/`
3. Now you'll set up a virtual environment so that the code runs locally:
   1. Enter `python3 -m venv env` You'll only need to do this the first time you run the script.
   2. Enter `source env/bin/activate` You'll need to do this every time you start a new session. If you see `(env)` in your terminal prompt, you've already done this and don't need to do it again.
   3. Enter `pip install -r requirements.txt` You only need to do this the first time you run the script. (gensim 4.3.2 cannot use recent releases of scipy due to [this issue](https://github.com/piskvorky/gensim/pull/3524). These requirements therefore specify an older version of scipy, but you may run into trouble if you already have a more recent version installed. As a workaround, if the script does not run, try installing an older version of scipy: pip install "scipy<1.13")
4. To run the script, type `python similar.py [word]`, substituting the word you want to explore for `[word]`. For example, to explore "surprise," type `python similar.py surprise`. The script will take a little while to run. Be patient! 
   1. By default, the script will return a list of "good neighbors" and a numerical representation of how similar/close they are to the word you're exploring in the Word2Vec space.
   2. If you would like to see a list of options available for customizing the output, type `python similar.py -h` or `python similar --help`
