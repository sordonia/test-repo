import torch
import argparse

parser = argparse.ArgumentParser("")
parser.add_argument("--data_dir", type=str)
parser.add_argument("--model_dir", type=str)
parser.add_argument("--log_dir", type=str)
args = parser.parse_args()

print(parser.model_dir)
