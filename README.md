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

## Usage

Encrypt PDF files with password protection:
```
pdfcipher enc file1.pdf file2.pdf file3.pdf
```

Decrypt PDF files:
```
pdfcipher dec file1.pdf file2.pdf file3.pdf
```

## License

Copyright (c) 2023-2025 [James Cherti](https://www.jamescherti.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

## Links

- [pdfcipher @GitHub](https://github.com/jamescherti/pdfcipher)
