import string
import numpy as np
import hashlib
import base64


def invert_permutation(p):
    s = np.empty_like(p)
    s[p] = np.arange(p.size)
    return s


class WeirdCipher:
    r"""
    Creates a WeirdCipher instance 

    Args:
        :param key: (``str``, required) the key to use

    Example:
        >>> cipher = WeirdCipher("some-key")
    """ 
    def __init__(self, key, encoding="utf-8"):
        self.encoding = encoding
        self.key = key

    def _generate_message_keys(self, message_size):
        encoding_bytes = {
            "utf-8": 8,
            "utf-16": 16
        }

        hash = hashlib.sha256()
        hash.update(self.key.encode(self.encoding))
        hash = hash.digest()

        message_key = [int(b) for b in hash]

        round_p = []
        round_k = []
        for key_byte in message_key:
            rng = np.random.RandomState(key_byte)
            
            round_p.append(rng.permutation(message_size))
            round_k.append(rng.randint(0, 2**encoding_bytes[self.encoding], message_size))
        
        return round_p, round_k


    def encrypt(self, message):
        r"""
        Encrypts a message

        Args:
            :param message: (``str``, required) the message to encrypt
        
        Example:
            >>> cipher = WeirdCipher("some-key")
            >>> ciphertext = cipher.encrypt("plaintext")
        
        """ 
        message = message.encode(self.encoding)
        round_p, round_k = self._generate_message_keys(len(message))

        message = np.array(bytearray(message))
        
        for p, k in zip(round_p, round_k):
            message = np.bitwise_xor(message, k)
            message = message[p]
            
        
        message = bytes(message.tolist())
        message = base64.b64encode(message)

        return message.decode("ascii")


    def decrypt(self, ciphertext):
        r"""
        Decrypts a message
        
        Args:
            :param ciphertext: (``str``, required) the ciphertext to decrypt

        Example:
            >>> cipher = WeirdCipher("some-key")
            >>> plaintext = cipher.decrypt("c+xJYDS+wrN+")
        
        """ 
        ciphertext = base64.b64decode(ciphertext)
        round_p, round_k = self._generate_message_keys(len(ciphertext))

        ciphertext = np.array(bytearray(ciphertext))
        for p, k in zip(round_p[::-1], round_k[::-1]):
            ciphertext = np.bitwise_xor(ciphertext, k)
            ciphertext = ciphertext[invert_permutation(p)]
        
        ciphertext = bytes(ciphertext.tolist())
        
        return ciphertext.decode(self.encoding)
        