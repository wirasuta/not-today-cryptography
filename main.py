import argparse
import time
import sys
from binascii import hexlify
from cipher import NotToday

def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='plaintext to be encrypted or ciphertext to be decrypted if -d is present', type=str)
    parser.add_argument('mode', help='mode of operation, available ECB/CBC/Counter', type=str)
    parser.add_argument('key', help='192 bit key', type=str)
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt input')
    parser.add_argument('-t', '--time', action='store_true', help='time the encryption')
    parser.add_argument('-x', '--hex', action='store_true', help='print in hex format')
    return parser.parse_args()

if __name__ == "__main__":
    args = init_argparse()
    not_today = NotToday(bytes(args.key, 'utf-8'), args.mode)

    if args.time:
        start = time.time()

    if args.decrypt:
        result = not_today.decrypt(bytes(args.input, 'utf-8'))
    else:
        result = not_today.encrypt(bytes(args.input, 'utf-8'))
    
    if args.hex:
        result = hexlify(result)
    print(result)

    if args.time:
        end = time.time()
        print(f'Elapsed time: {end - start:.5g}', file=sys.stderr)