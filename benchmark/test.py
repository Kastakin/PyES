import argparse
import json

from src.main.python.optimizers.distribution import Distribution

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="JSON input file")
    args = parser.parse_args()

    with open(args.file, "r") as input_file:
        data = json.load(input_file)

    opt = Distribution()
    opt.fit(data)
    opt.predict()
