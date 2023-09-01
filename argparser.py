import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=False, default = "test")
parser.add_argument('--id', type=str, required=False)
parser.add_argument('--env', type=str, required=True)
args = parser.parse_args()

print (args.__dict__)