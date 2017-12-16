def superEncrypt(text,rot):


    def alphabet_position(letter):
        return ((ord(letter.upper()) - 65))


    def rotate_character(char, rot):
        if not char.isalpha():
            return char
        pos = alphabet_position(char)
        mutator = 65
        if ord(char) >= 97:
            mutator = 97
        new_pos = ((pos + rot) % 26) + mutator
        return (chr(new_pos))

    def encrypt(text, rot):
        encrypted_text = ""
        for i in text:
            encrypted_text += rotate_character(i, rot)
        return encrypted_text

    return encrypt(text,rot)