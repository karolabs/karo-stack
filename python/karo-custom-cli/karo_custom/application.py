# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging

from karo_custom.config import load_config

log = logging.getLogger(__name__)


def run(run_apply: bool) -> None:
    config = load_config()
    log.debug(f"{config=}")
