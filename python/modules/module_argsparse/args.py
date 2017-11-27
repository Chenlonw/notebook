# -*- coding: utf-8 -*-
import subprocess
import argparse

parser = argparse.ArgumentParser()
# positional arguments
parser.add_argument("echo", help="echo is a test argument")
parser.add_argument("-s", "--square", help="input to be squared", type=int,
                    choices=[0, 1, 2])
# optional arguments
parser.add_argument("--verbosity", help="increase output verbosity",
                    action="store_true") # action 默认的参数选择

parser.add_argument("-v", "--shortverbosity", help="increase output verbosity")

args = parser.parse_args()

print ('echo:', args.echo)
print ('square:', args.square)
if args.verbosity:
    print(args.verbosity)
    print('verbosity on')

if args.shortverbosity:
    print('short verbosity on')
    print('-v', args.shortverbosity)

# python args.py 1 --verbosity -s 2 -v 2
