import argparse
import time
import sys
from binascii import hexlify
from cipher import NotToday

def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='plaintext to be encrypted or ciphertext to be decrypted if -d is present')
    parser.add_argument('mode', help='mode of operation, available ECB/CBC/Counter')
    parser.add_argument('key', help='192 bit key')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt input')
    parser.add_argument('-t', '--time', action='store_true', help='time the encryption')
    parser.add_argument('-x', '--hex', action='store_true', help='print in hex format')
    args = parser.parse_args()

if __name__ == "__main__":
    init_argparse()
    not_today = NotToday(bytes(args.key), args.mode)

    if args.time:
        start = time.time()

    if args.decrypt:
        result = not_today.decrypt(bytes(args.input))
    else:
        result = not_today.encrypt(bytes(args.input))
    
    if args.hex:
        result = hexlify(result)
    print(result)

    if args.time:
        end = time.time()
        print(f'Elapsed time: {start - end}', file=sys.stderr)