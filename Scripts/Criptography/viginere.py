# -*- coding: utf-8 -*-
__author__ = 'Bruno Paes'
__email__ = 'brunopaes05@gmail.com'
__github__ = 'https://www.github.com/Brunopaes'
__status__ = 'Finalised'


class Viginere(object):

    @staticmethod
    def encrypt(plaintext, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext


if __name__ == '__main__':
    c = Viginere()
    print(c.decrypt('efsdsetpe', 'espm'))