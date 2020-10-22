from typing import List
from config import *

class NotToday(object):
    def __init__(self, key: bytes, mode: str):
        self.external_key = key
        self.mode = mode
        self.subkeys = self._key_scheduler(self.external_key, ROUND_NUM)
    
    def encrypt(plaintext: bytes) -> bytes:
        pass

    def decrypt(ciphertext: bytes) -> bytes:
        pass

    def _feistel_net(block: bytes, round_key: bytes) -> bytes:
        pass

    def _f_function(half_block: bytes, round_key: bytes) -> bytes:
        pass

    def _key_scheduler(external_key: bytes, round: int) -> List[bytes]:
        pass