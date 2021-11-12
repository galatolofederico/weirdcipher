from weirdcipher import WeirdCipher


messages_keys = [
    dict(
        key="key-1",
        msg="ciao"
    ),
    dict(
        key="key-2",
        msg="hello"
    ),
    dict(
        key="key-3",
        msg="hello world"
    )
]


def test_fixed_messages():
    for mk in messages_keys:
        cipher = WeirdCipher(mk["key"])
        ciphertext = cipher.encrypt(mk["msg"])
        plaintext = cipher.decrypt(ciphertext)

        assert mk["msg"] == plaintext

