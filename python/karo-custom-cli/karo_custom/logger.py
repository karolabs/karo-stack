# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging


def configure_logging(debug: bool) -> None:
    log_level = "DEBUG" if debug else "WARNING"

    # capitalise log level names (INFO -> Info)
    for level in (
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    ):
        logging.addLevelName(level, logging.getLevelName(level).capitalize())

    # set global logging config
    logging.basicConfig(level=log_level, format="%(levelname)s: %(name)s: %(message)s")
