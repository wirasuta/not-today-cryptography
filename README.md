# Not Today Cryptography

TL;DR

```bash
$ python3 main.py -h                                                  
usage: main.py [-h] [-i INPUT] [-f FILE] [-d] [-t] [-x] mode key

positional arguments:
  mode                  mode of operation, available ECB/CBC/Counter
  key                   192 bit key

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        plaintext to be encrypted or ciphertext to be decrypted if -d is present
  -f FILE, --file FILE  input file
  -d, --decrypt         decrypt input
  -t, --time            time the encryption
  -x, --hex             print in hex format

# Encrypt string "ABBBBBBBBBBBBBBB" with mode "ECB" and key "aaaabbbbccccddddeeeeffff"
$ python3 main.py -t -i ABBBBBBBBBBBBBBB ECB aaaabbbbccccddddeeeeffff > ./result/out.enc
Elapsed time: 0.00018954

# Decrypt previously encrypted string, print result in hex
$ python3 main.py -t -d -x -f ./result/out.enc ECB aaaabbbbccccddddeeeeffff
b'41424242424242424242424242424242'
Elapsed time: 0.00026226
```