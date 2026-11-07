# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging
import tomllib
from pathlib import Path

from karo_custom.errors import ConfigError

log = logging.getLogger(__name__)

CONFIG_FILE = Path("./karo-custom.toml")


def load_config() -> dict:
    """Return data from a valid `karo-custom.toml` config."""

    log.debug(f"Loading config '{CONFIG_FILE}'")

    # read config file
    try:
        with open(CONFIG_FILE, "rb") as file:
            config_data = tomllib.load(file)

    except FileNotFoundError as exc:
        raise ConfigError(f"Configuration file not found: '{CONFIG_FILE}'") from exc

    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"Invalid TOML configuration: {exc}") from exc

    except OSError as exc:
        raise ConfigError(f"Unable to read configuration file: {exc}") from exc

    return config_data
