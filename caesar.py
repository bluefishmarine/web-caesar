class Encryption:

    # def __init__(self):
    #     return 0


    def alphabet_position(self,letter):
        return ((ord(letter.upper()) - 65))


    def rotate_character(self,char,rot):
        if not char.isalpha():
            return char
        pos = self.alphabet_position(char)
        mutator = 65
        if ord(char) >= 97:
            mutator = 97
        new_pos = ((pos + rot) % 26) + mutator
        return (chr(new_pos))

    def encrypt(self,text,rot):
        encrypted_text = ""
        for i in text:
            encrypted_text += self.rotate_character(i, rot)
        return encrypted_text

    def text_encrypt(self,text,key):
        new_text = ""
        count = -1
        for i in range(0, len(text)):
            count += 1
            if not text[i].isalpha():
                count -= 1
            pos = count % len(key)
            rot = self.alphabet_position(key[pos])
            new_text += self.rotate_character(text[i], rot)
        return new_text    