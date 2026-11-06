# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import argparse
import logging

from karo_custom import logger
from karo_custom.errors import ExpectedError

log = logging.getLogger(__name__)


def main() -> int:

    parser = argparse.ArgumentParser(prog="karo_custom", add_help=False)

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit.",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output.",
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Generate 'karo-custom.toml' defined file structure.",
    )

    args = parser.parse_args()

    logger.configure_logging(args.debug)

    try:
        if args.apply:
            print("apply")
        else:
            print("lint only")

    except ExpectedError as exc:
        log.error(exc)
        return 1

    return 0
