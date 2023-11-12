def tohex(message):
    # verification = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    # conversion to hex based on order

    enc_message = ''

    for i in message:
        if i == ' ':
            enc_message += " "
        if i in "0123456789":
            enc_message += f' n{i}'
        else:
            enc_message += str(hex(ord(i)))[2:]

    return enc_message


if __name__ == '__main__':
    mess = True
    while mess:
        mess = input()
        if not mess:
            break
        print(f'encrypted message = {tohex(mess)}')
