#!/usr/bin/env python3
import os
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser("Text Similarity")
    parser.add_argument("directory", help="Directory containing .txt files")
    return parser.parse_args()


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
        with open(file, 'r') as src_file:
            src_file.read()


def main():
    args = parse_args()
    load_sources(args.directory)


if __name__ == "__main__":
    main()
