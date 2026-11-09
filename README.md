# pdfcipher - A command-line tool for encrypting and decrypting PDF files with password protection
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI Version](https://img.shields.io/pypi/v/pdfcipher.svg)](https://pypi.org/project/pdfcipher/)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white)

- Author: James Cherti <[https://www.jamescherti.com/](https://www.jamescherti.com/)>
- License: GPL 3.0 or later

The **[pdfcipher](https://github.com/jamescherti/pdfcipher)** command-line tool enables encrypting and decrypting PDF files with password-based protection. It sets or removes passwords on individual PDF files or entire directory trees, updating the files in place.

## Features

- Encrypts and decrypts PDF documents using 256-bit AES encryption via `qpdf`.
- Supports passing individual files, directories, or a mix of both.
- Recursively searches directories to find and process all PDF files.
- Updates files in place safely using temporary files to avoid partial writes.
- Handles file paths containing spaces, parentheses, and other special characters.
- Validates passwords with confirmation on encryption, and prompts again if a file requires a different password during decryption.

## Requirements

- Python 3.10 or later
- The [qpdf](https://github.com/qpdf/qpdf) command-line tool

## Installation

To install the *pdfcipher* executable locally in `~/.local/bin/` using [pip](https://pypi.org/project/pip/), run:

```bash
pip install --user pdfcipher
```

(Omitting the `--user` flag will install *pdfcipher* system-wide in `/usr/local/bin/`.)

## Usage

```text
pdfcipher [--option] {enc,dec} files_or_dirs [files_or_dirs ...]
```

### Encrypt

Encrypt PDF files or directory trees:

```bash
pdfcipher enc file1.pdf "my document (draft).pdf" /path/to/folder/
```

The tool prompts for a password and a confirmation password. It then encrypts the target files in place using 256-bit AES encryption. When directories are supplied, *pdfcipher* searches them recursively and processes every discovered PDF.

### Decrypt

Decrypt PDF files or directory trees:

```bash
pdfcipher dec file1.pdf "my document (draft).pdf" /path/to/folder/
```

The tool prompts for the password and removes encryption from the files in place. If an individual file fails decryption due to a mismatched password, *pdfcipher* prompts for the correct password and continues processing the remaining files.

## License

Copyright (c) 2023-2026 [James Cherti](https://www.jamescherti.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

## Links

- [pdfcipher @GitHub](https://github.com/jamescherti/pdfcipher)
- [pdfcipher @PyPI](https://pypi.org/project/pdfcipher/)
