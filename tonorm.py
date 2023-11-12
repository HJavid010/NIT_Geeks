def tonorm(enc):
    message = ''
    parts = enc.split()
    # print(parts)
    for part in parts:

        if len(part) == 1:
            message += part
        else:
            for j in range(0, len(part) - 1, 2):
                p_hex = '0x'
                p_hex += part[j:j + 2]
                # print(f'hexa part = {p_hex}')
                message += chr(int(p_hex, 16))
    return message


if __name__ == '__main__':
    enc_m = True
    while enc_m:
        enc_m = input()
        if not enc_m:
            break
        print(tonorm(enc_m).lower())
