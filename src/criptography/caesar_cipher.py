# -*- coding: utf-8 -*-
__author__ = 'Bruno Paes'
__email__ = 'brunopaes05@gmail.com'
__github__ = 'https://www.github.com/Brunopaes'
__status__ = 'Finalised'


class Caesar(object):
    def __init__(self):
        """Initialises the alphabet dictionaries and the first question
        (encrypt or decrypt).

        alphabet = {
            'A': 0,
            'B': 1,
            'C': 2
        }

        alphabet2 = {
            0: 'A',
            1: 'B',
            2: 'C'
        }
        """
        self.alphabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
        self.alphabet2 = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        self.text = ''
        self.qst = self.qst1()
        self.qst_2 = ''
        self.key = 0

    # Used in main
    def encrypt(self):
        """
        This method, after receiving the plain message and key, crypto the
        plain message with the provided key.

        :return text: Encrypted text

        """
        text = ''
        for letter in self.text.upper():
            if letter.isalpha():
                text += self.alphabet2[(self.alphabet[letter] + self.key) % 26]
            else:
                text += letter
        return text

    # Used in main
    def decrypt(self):
        """
        This method, after receiving the crypto message and key, decrypt the
        plain message with the provided key.

        :return text: Decrypted text

        """
        text = ''
        for letter in self.text.upper():
            if letter.isalpha():
                text += self.alphabet2[(self.alphabet[letter] - self.key) % 26]
            else:
                text += letter
        return text

    def main(self):
        if self.qst == 1:
            self.text = input('Input your to be encrypted message\n')
            try:
                self.key = int(input('Input your key\n'))
                print(self.encrypt())
            except ValueError as e:
                print('Please, insert an Integer Value\n{}'.format(e.args))
        else:
            self.text = input('Input your to be decrypted message\n')
            self.qst_2 = self.qst_2()
            if self.qst_2 == 1:
                for i in range(1, 26):
                    self.key = i
                    print('Rotation {}: {}'.format(i, self.decrypt()))
            else:
                try:
                    self.key = int(input('Input your key\n'))
                    print(self.decrypt())
                except ValueError as e:
                    print('Please, insert an Integer Value\n{}'.format(e.args))

    # Used in constructor
    @staticmethod
    def qst1():
        try:
            return int(input('Do you want to ENCRYPT [1] or DECRYPT [2]\n'))
        except ValueError as e:
            print('Please, insert an Integer Value\n{}'.format(e.args))

    # Used in main
    @staticmethod
    def qst2():
        try:
            return int(input('Do you want to test all possibilities? '
                             'YES [1] or NO [2]\n'))
        except ValueError as e:
            print('Please, insert an Integer Value\n{}'.format(e.args))


if __name__ == '__main__':
    obj = Caesar()
    obj.main()
