from typing import List
from config import *
from utils import *

class NotToday(object):
    def __init__(self, key: bytes, mode: str):
        self.external_key = key
        self.mode = mode
        self.subkeys = self._key_scheduler(self.external_key, ROUND_NUM)
    
    def encrypt(self, plaintext: bytes) -> bytes:
        pass

    def decrypt(self, ciphertext: bytes) -> bytes:
        pass

    def _feistel_net(self, block: bytes) -> bytes:
        total_length = len(block)
        half_length = total_length // 2
        l = block[0:half_length]
        r = block[half_length:total_length]

        for i in range(16):
            new_r = l ^ self._f_function(r, self.subkeys[i])
            l = r
            r = new_r

        return l + r


def _f_function(half_block: bytes, round_key: bytes) -> bytes:
    temp = bytes()
    half_block_roll = half_block[0] % 64
    round_key_roll = round_key[0] % 64

    for i in range(8):
        new_value = roll_int_right(half_block[i], half_block_roll) ^ roll_int_right(round_key[i], round_key_roll)
        temp = temp + bytes([new_value])

    # S-Box substitution here

    return roll_bits_right(temp, temp[7])

    def _key_scheduler(self, external_key: bytes, round: int) -> List[bytes]:
        if len(external_key) * 8 != 192:
            raise Exception('Invalid key size')
            
        if round % 3 != 0:
            raise Exception('Invalid round number')

        keys = [external_key[i*8:(i+1)*8] for i in range(3)]

        for i in range(round//3):
            temp = []
            temp.append(roll_bits_right(xor_bytes(keys[-3], keys[-2]), i))
            temp.append(roll_bits_right(xor_bytes(keys[-3], keys[-1]), i+1))
            temp.append(roll_bits_right(xor_bytes(keys[-2], keys[-1]), i+2))
            keys.extend(temp)

        keys = keys[3:]
        return keys