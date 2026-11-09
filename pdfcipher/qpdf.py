#!/usr/bin/env python3
#
# Copyright (c) 2023-2026 James Cherti
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
"""Encrypt/Decrypt PDF files using qpdf."""

import logging
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from .vars import FLAG_MODE_DECRYPT, FLAG_MODE_ENCRYPT

QPDF_BIN = "qpdf"


class Qpdf:
    """Wrapper around the qpdf command-line utility."""

    def __init__(self) -> None:
        """Initialize the Qpdf wrapper."""
        self.qpdf_cmd = QPDF_BIN
        self._logger = logging.getLogger(sys.argv[0])

    def decrypt(
        self,
        input_file: str | Path,
        output_file: str | Path,
        password: str,
    ) -> None:
        """Decrypt a PDF file using the provided password."""
        self._generic_qpdf_encdec(
            input_file=input_file,
            output_file=output_file,
            password=password,
            mode=FLAG_MODE_DECRYPT,
        )

    def encrypt(
        self,
        input_file: str | Path,
        output_file: str | Path,
        password: str,
    ) -> None:
        """Encrypt a PDF file using the provided password."""
        self._generic_qpdf_encdec(
            input_file=input_file,
            output_file=output_file,
            password=password,
            mode=FLAG_MODE_ENCRYPT,
        )

    def _generic_qpdf_encdec(
        self,
        input_file: str | Path,
        output_file: str | Path,
        mode: int,
        password: str,
    ) -> None:
        tmp_path: Path | None = None
        try:
            # Close the file descriptor returned by mkstemp to prevent FD leaks.
            fd, raw_tmp_path = tempfile.mkstemp(prefix="pdfcipher", suffix=".pdf")
            os.close(fd)
            tmp_path = Path(raw_tmp_path)

            if mode == FLAG_MODE_ENCRYPT:
                read_password = password
                owner_password = password
                qpdf_args = [
                    "--encrypt",
                    read_password,
                    owner_password,
                    "256",
                    "--",
                    str(input_file),
                    str(tmp_path),
                ]
            elif mode == FLAG_MODE_DECRYPT:
                qpdf_args = [
                    "--decrypt",
                    f"--password={password}",
                    "--",
                    str(input_file),
                    str(tmp_path),
                ]
            else:
                raise ValueError("Mode can only be MODE_ENCRYPT or MODE_DECRYPT")

            self._run_qpdf(qpdf_args)
            shutil.copy(tmp_path, output_file)
        finally:
            if tmp_path is not None:
                tmp_path.unlink(missing_ok=True)

    def _run_qpdf(self, args: list[str]) -> None:
        try:
            # stdout subprocess to DEVNULL to prevent it from printing:
            # WARNING: file.pdf (object 2032 0, offset 470342): dictionary has
            # duplicated key /Author; last occurrence overrides earlier ones
            # qpdf: operation succeeded with warnings; resulting file may have
            # some problems
            cmd = [self.qpdf_cmd, *args]
            self._logger.debug("[RUN] %s", subprocess.list2cmdline(cmd))
            subprocess.check_call(cmd, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError as err:
            # 3 = qpdf warnings
            if err.returncode != 3:
                raise
