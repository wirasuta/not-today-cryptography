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

    def _feistel_net(self, block: bytes, round_key: bytes) -> bytes:
        pass

    def _f_function(self, half_block: bytes, round_key: bytes) -> bytes:
        pass

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