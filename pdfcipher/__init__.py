#!/usr/bin/env python
#
# Copyright (c) 2023-2025 James Cherti
# URL: https://github.com/jamescherti/pdfcipher
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
"""The entry-point of pdfcipher."""


import argparse
import logging
import subprocess
import sys

from .helpers import input_password
from .qpdf import Qpdf
from .vars import FLAG_MODE_DECRYPT, FLAG_MODE_ENCRYPT


def pdfcypher_run(mode: int, file_or_dirs: list):
    if mode == FLAG_MODE_ENCRYPT:
        password = input_password()
        password2 = input_password("Re-enter the password for confirmation: ")
        if password != password2:
            print("Error: Passwords do not match.", file=sys.stderr)
            sys.exit(1)
    else:
        password = input_password()

    pdf = Qpdf()

    for file in file_or_dirs:
        if mode == FLAG_MODE_ENCRYPT:
            print("[ENCRYPT]", file)
        else:
            print("[DECRYPT]", file)

        current_password = password
        while True:
            try:
                if mode == FLAG_MODE_ENCRYPT:
                    pdf.encrypt(file, file, current_password)
                else:
                    pdf.decrypt(file, file, current_password)
            except subprocess.CalledProcessError as err:
                if err.returncode == 2:
                    # The exit-code 2 means that the password is invalid
                    current_password = input_password()
                else:
                    print("Error: qpdf returned non-zero exit code",
                          err.returncode,
                          file=sys.stderr)
                    sys.exit(1)
            else:
                break


def parse_args():
    """Parse command-line arguments for encryption or decryption actions."""
    usage = "%(prog)s [--option] [args]"
    parser = argparse.ArgumentParser(
        description=("A command-line tool for encrypting and decrypting PDF "
                     "files with password protection."),
        usage=usage)

    parser.add_argument("action", type=str, choices=["enc", "dec"],
                        help="Action: 'enc' for encrypt or 'dec' for decrypt")

    parser.add_argument("files_or_dirs", metavar="N", type=str, nargs="+",
                        help="PDF files to encrypt or decrypt")

    return parser.parse_args()


def command_line_interface():
    """The command-line interface."""
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="[INFO] %(name)s: %(message)s")

    args = parse_args()
    if args.action == "enc":
        pdfcypher_run(FLAG_MODE_ENCRYPT, args.files_or_dirs)
    elif args.action == "dec":
        pdfcypher_run(FLAG_MODE_DECRYPT, args.files_or_dirs)


if __name__ == "__main__":
    command_line_interface()
