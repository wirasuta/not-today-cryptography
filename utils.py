def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x,y in zip(a,b)])

def roll_bytes_right(a: bytes, n: int) -> bytes:
    pass

def roll_bits_right(a: bytes, n: int) -> bytes:
    temp = int.from_bytes(a, 'little')
    temp = temp >> n | ((temp << (64 - n)) & 0xFFFFFFFF)
    return temp.to_bytes(8, 'little')

def roll_int_right(a: int, n: int) -> int:
    n = n % 8
    temp = a >> n | (a << (8 - n)) & 0xFF
    return temp