import hashlib

def obfuscate_string(input_str, seed):
    sha1 = hashlib.sha1()
    array = (seed + input_str).encode('utf-32le')
    sha1.update(array)
    hash_val = sha1.digest()
    return sha1_to_bee_str(hash_val)

def sha1_to_bee_str(hash_val):
    byte_array = bytearray(hash_val)
    bee_str = []
    num2 = 4
    num3 = 0
    i = 0

    while i < 6:
        num4 = byte_array[i]
        j = 8

        while j > 0:
            if num2 == 0:
                bee_str.append(get_char(65 + num3))
                num3 = 0
                num2 = 4
            
            num5 = min(j, num2)
            num6 = 2 ** num5
            num3 += num4 % num6
            num2 -= num5
            num3 <<= num2
            j -= num5
            num4 >>= num5
        
        i += 1
    
    bee_str.append('\0')
    return ''.join(bee_str)

def get_char(value):
    num = 0
    for num2 in [33, 35, 36, 37, 38, 47, 92, 95, 46, 0]:
        if value + num >= num2 and 65 <= num2:
            num += 1
    
    return chr(value + num)

if __name__ == '__main__':
    print(obfuscate_string("__clearAll", "69f38d77aa560f61"))
    # ODJOAGFAILG⇨__clearAll