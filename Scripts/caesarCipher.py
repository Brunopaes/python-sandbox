class Cipher(object):
    def __init__(self, key, plaintext):
        self.alphabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
        self.alphabet2 = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.key = key
        self.plaintext = plaintext

    def encipher(self):
        ciphertext = ''
        for c in self.plaintext.upper():
            if c.isalpha():
                ciphertext += self.alphabet2[(self.alphabet[c] + self.key) % 26]
            else:
                ciphertext += c
        print('encrypted message: {}'.format(ciphertext))
        return ciphertext

    def decipher(self, ciphertext):
        plaintext = ""
        for c in ciphertext.upper():
            if c.isalpha():
                plaintext += self.alphabet2[(self.alphabet[c] - self.key) % 26]
            else:
                plaintext += c
        print('decrypted message: {}'.format(plaintext))


if __name__ == '__main__':
    while (True):
        try:
            x = int(input('INPUT YOUR KEY: '))
            c = Cipher(x, input('INPUT YOUR MESSAGE: '))
            x = c.encipher()
            # c.decipher(x)
        except Exception as e:
            print(e.args)