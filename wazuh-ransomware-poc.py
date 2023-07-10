#!/usr/bin/env python3

# Copyright (C) 2015-2019, Wazuh Inc.
# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import os
import random
import string
import base64
import sys
from pathlib import Path
from cryptography.fernet import Fernet


def create_random_files(basedir, n_directories, n_files_per_directory, size_file=1024):

    for root, dirs, files in os.walk(str(basedir)):
        for n_dir in range(n_directories):
            p = Path(root) / 'Directory_{}'.format(str(n_dir).zfill(2))
            p.mkdir(exist_ok=True)

    for root, dirs, files in os.walk(str(basedir)):
        if root is basedir:
            continue

        for n_file in range(n_files_per_directory):
            new_file = '{}/File_{}.txt'.format(root, str(n_file).zfill(2))
            text = ''.join([random.choice(string.ascii_letters) for i in range(size_file)]) #1
            with open(new_file, 'w') as f:
                f.write(text)

    return None


def encrypt_file(filepath, plain_key, output_filepath):
    
    encoded_key = base64.urlsafe_b64encode(plain_key.encode())

    # Encrypt file using cryptography.fernet library
    with open(filepath, mode='rb') as f_clear:
        fernet_cipher = Fernet(encoded_key)
        encrypted_data = fernet_cipher.encrypt(f_clear.read())
    
    # Remove sensitive variables
    del plain_key, encoded_key
    
    # Write content to file
    with open(output_filepath, mode='wb') as f_encrypt:
        f_encrypt.write(encrypted_data)


def decrypt_file(filepath, plain_key, output_filepath):
    
    encoded_key = base64.urlsafe_b64encode(plain_key.encode())

    # Decrypt file using cryptography.fernet library
    with open(filepath, mode='rb') as f_clear:
        fernet_cipher = Fernet(encoded_key)
        clear_data = fernet_cipher.decrypt(f_clear.read())
    
    # Remove sensitive variables
    del plain_key
    
    # Write content to file
    with open(output_filepath, mode='wb') as f_encrypt:
        f_encrypt.write(clear_data)


def encrypt_files(basedir, key):

    # Read operation
    for root, dirs, files in os.walk(str(basedir)):
        for file in files:
            # Write operation
            src_file = os.path.join(root, file)
            dst_file = '{}.{}'.format(src_file, "encrypted")
            encrypt_file(src_file, key, dst_file)
            # Delete operation
            os.remove(src_file)


def decrypt_files(basedir, key):

    # Read operation
    for root, dirs, files in os.walk(str(basedir)):
        for file in files:
            if file.endswith('.encrypted'):
                # Write operation
                src_file = os.path.join(root, file)
                dst_file = os.path.splitext(src_file)[0]
                decrypt_file(src_file, key, dst_file)
                # Delete operation
                os.remove(src_file)


if __name__ == '__main__':
    try:
        action = sys.argv[1]
    except:
        print("Error: Bad arguments. Valid arguments: 'prepare', 'attack', 'restore'")
        sys.exit(1)

    basedir = "/home/vagrant/test"
    key = "nso42FGdswR0805tnVqeww0u3Rubwk2a"

    if action == "prepare":
        create_random_files(basedir, n_directories=10, n_files_per_directory=20, size_file=1024)
    elif action == "attack":
        encrypt_files(basedir, key)
    elif action == "restore":
        decrypt_files(basedir, key)


