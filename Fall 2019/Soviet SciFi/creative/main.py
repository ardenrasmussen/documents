#!/usr/bin/env python3
import os
import json
import nltk
import numpy as np
from collections import Counter
from argparse import ArgumentParser
from num2words import num2words

from pprint import pprint


def parse_args():
    parser = ArgumentParser("Text Similarity")
    parser.add_argument("directory", help="Directory containing .txt files")
    return parser.parse_args()


def convert_lower_case(data):
    return np.char.lower(data)


def remove_stop_words(data):
    stop_words = nltk.corpus.stopwords.words('english')
    words = nltk.tokenize.word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text


def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data


def remove_apostrophe(data):
    return np.char.replace(data, "'", "")


def stemming(data):
    stemmer = nltk.stem.PorterStemmer()
    tokens = nltk.tokenize.word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text


def convert_numbers(data):
    tokens = nltk.tokenize.word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        try:
            w = num2words(int(w))
        except:
            pass
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text


def preprocess(data):
    data = convert_lower_case(data)
    data = remove_punctuation(data)
    data = remove_apostrophe(data)
    data = remove_stop_words(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = remove_stop_words(data)
    return data


def tokenize_source(src):
    return nltk.tokenize.word_tokenize(src)


def load_sources(directory):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f.endswith("txt")
    ]
    sources = {}
    for file in files:
        print("Loading {}...".format(file))
        with open(file, 'r', errors='ignore') as src_file:
            sources[file.split('/')[-1]] = tokenize_source(
                preprocess(src_file.read()))
    return sources


def jaccard_similarity(txt_a, txt_b):
    intersection = set(txt_a).intersection(set(txt_b))
    union = set(txt_a).union(set(txt_b))
    return len(intersection) / len(union)


def calculate_df(sources):
    DF = {}
    for key in sources:
        for w in sources[key]:
            try:
                DF[w].add(key)
            except:
                DF[w] = {key}
    for i in DF:
        DF[i] = len(DF[i])
    return DF


def matching(query, tf_idf):
    query_weights = {}
    for key in tf_idf:
        if key[1] in query:
            try:
                query_weights[key[0]] += tf_idf[key]
            except:
                query_weights[key[0]] = tf_idf[key]
    query_weights = sorted(query_weights.items(),
                           key=lambda x: x[1],
                           reverse=True)
    return {x[0]: x[1] for x in query_weights}


def generate_fdg(sources, tf_idf):
    nodes = []
    links = []
    for idx, src in enumerate(sources):
        print("Computing {}...".format(src))
        nodes.append({"name": src, "group": idx})
        weights = matching(src, tf_idf)
        for idy, dest in enumerate(sources):
            if idx == idy:
                continue
            if dest in weights and weights[dest] > 1e-4:
                links.append({
                    "source": idx,
                    "target": idy,
                    "value": weights[dest]
                })
            else:
                print("FAILS: {}-{}".format(src, dest))
    with open("pcap_export.json", 'w') as out_file:
        out_file.write(
            json.dumps({
                "nodes": nodes,
                "links": links
            }, sort_keys=True))


def main():
    args = parse_args()
    sources = load_sources(args.directory)
    DF = calculate_df(sources)
    tf_idf = {}
    for key in sources:
        counter = Counter(sources[key])
        word_count = len(sources[key])
        for token in np.unique(sources[key]):
            tf = counter[token] / word_count
            if token in DF:
                df = DF[token]
            else:
                df = 0
            # idf = np.log((len(sources) + 1) / (df + 1))
            idf = (len(sources) + 1) / (df + 1)
            tf_idf[key, token] = tf * idf
    generate_fdg(sources, tf_idf)


if __name__ == "__main__":
    main()
