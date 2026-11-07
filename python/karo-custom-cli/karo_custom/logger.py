# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import copy
import logging

LOG_FORMAT = "%(levelname)s: %(name)s: %(message)s"

# ansi colour codes
LEVEL_NAME_COLOURS = {
    logging.DEBUG: "\033[90m",  # bright black
    logging.INFO: "\033[32m",  # green
    logging.WARNING: "\033[33m",  # yellow
    logging.ERROR: "\033[31m",  # red
    logging.CRITICAL: "\033[91m",  # bright red
}
NAME_COLOUR = "\033[36m"  # cyan
RESET = "\033[0m"


class CustomFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        # prevent overwriting original record
        record = copy.copy(record)

        # prepare log level formatting
        level_colour = LEVEL_NAME_COLOURS.get(record.levelno, "")
        level_name = record.levelname.capitalize()  # INFO -> Info

        # apply ansi colour escape codes
        record.levelname = f"{level_colour}{level_name}{RESET}"
        record.name = f"{NAME_COLOUR}{record.name}{RESET}"

        return super().format(record)


def configure_logging(debug: bool) -> None:
    # apply custom formatting
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter(LOG_FORMAT))

    # set global logging config
    log_level = logging.DEBUG if debug else logging.WARNING

    logging.basicConfig(
        level=log_level,
        handlers=[handler],
    )
