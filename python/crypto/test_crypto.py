from file_crypto import Crypto
from pathlib import Path

def test_crypto(tmp_path):
    p = tmp_path / 'test.txt'
    with open(p, 'w') as file:
        file.write('hello world')
    t_c = Crypto(p, None)
    t_c.crypto_f()
    t_c = Crypto(p, str(tmp_path / 'Ckey.txt'))
    t_c.decrypto_f()
    with open(p, 'r') as file:
        data = file.read()
    assert data == "hello world"

def test_enc(tmp_path):    
    p = tmp_path / 'test2.txt'
    with open(p, 'w') as file:
        file.write('hello world')
    t_c = Crypto(p, None)
    t_c.crypto_f()
    assert Path(str(p) + '.enc').exists()

def test_key(tmp_path):
    p = tmp_path / 'test3.txt'
    with open(p, 'w') as file:
        file.write('hello world')
    t_c = Crypto(p, None)
    t_c.crypto_f()
    t_c = Crypto(p, str(tmp_path / 'Ckey.txt'))
    t_c.decrypto_f()
    assert not (tmp_path / 'Ckey.txt').exists() 
    assert not Path(str(p) + '.enc').exists()
