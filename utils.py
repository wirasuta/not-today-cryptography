from typing import List

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x,y in zip(a,b)])

def roll_bytes_right(a: bytes, n: int) -> bytes:
    pass

def roll_bits_right(a: bytes, n: int) -> bytes:
    temp = int.from_bytes(a, 'little')
    temp = temp >> n | ((temp << (64 - n)) & 0xFFFFFFFF)
    return temp.to_bytes(8, 'little')

def text_to_blocks(t: bytes, block_size: int) -> List[bytes]:
    t_len = len(t)
    padding_size = (block_size * (t_len // block_size + 1)) % t_len
    
    temp = [b for b in t] + [padding_size - 1 for _ in range(padding_size)] 
    temp = [temp[i*block_size:(i+1)*block_size] for i in range()]

    return temp

def all_same(items):
    """ https://stackoverflow.com/a/3787983/3134677 """
    return all(x == items[0] for x in items)

def blocks_to_text(blocks: List[bytes]) -> bytes:
    temp = b''.join(blocks)
    last_byte = temp[-1]
    if temp >= 0 and temp <= 14 and all_same(temp[-1-last_byte:]):
        temp = temp[:-1-last_byte]
    return temp

def switch_half_blocks(block: bytes, block_size: int) -> bytes:
    return bytes([block[block_size//2:], block[:block_size//2]])
