from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    #Em python um array de bytes podem ser usados de maneira mais performática como um grande inteiro
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key:int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int)->str:
    decripted: int = key1 ^ key2
    temp: bytes = decripted.to_bytes((decripted.bit_length() + 7 //8), "big")
    return temp.decode()


    
if(__name__ == "__main__"):
    print(decrypt(*encrypt("Adamastor")))
