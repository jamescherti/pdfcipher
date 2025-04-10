# pdfcipher - A command-line tool for encrypting and decrypting PDF files with password protection
![License](https://img.shields.io/github/license/jamescherti/pdfcipher)

The **pdfcipher** command-line tool enables encrypting and decrypting PDF files with password-based encryption. It allows users to set and remove passwords, ensuring secure access and distribution of PDF documents.

## Requirements

- The [qpdf](https://github.com/qpdf/qpdf) command-line tool.

## Installation

To install the *pdfcipher* executable locally in `~/.local/bin/` using [pip](https://pypi.org/project/pip/), run:
```
pip install --user pdfcipher
```

(Omitting the `--user` flag will install *pdfcipher* system-wide in `/usr/local/bin/`.)

### Encrypt

Encrypt PDF files with password protection:
```
pdfcipher enc file1.pdf file2.pdf file3.pdf
```

The tool will prompt the user to enter a password, which will then be used to encrypt all the specified PDF files:

### Decrypt

Decrypt PDF files by entering the password used for encryption:
```
pdfcipher dec file1.pdf file2.pdf file3.pdf
```

If the entered password is correct, the tool will attempt to use it for all the other files. If any file fails to be decrypted, the tool will prompt you to re-enter the password for convenience:

## License

Copyright (c) 2023-2025 [James Cherti](https://www.jamescherti.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

## Links

- [pdfcipher @GitHub](https://github.com/jamescherti/pdfcipher)
- [pdfcipher @PyPI](https://pypi.org/project/pdfcipher/)
