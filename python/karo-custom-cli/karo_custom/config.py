# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging
import re
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

    validate_config(config_data)

    return config_data


def validate_config(config_data: dict) -> None:
    """Validate `karo-custom.toml` configuration data."""

    log.debug("Validating config")

    KEYS = (
        "spec_version",
        "username",
        "author",
        "license",
        "dependencies",
        "compose",
    )

    REQUIRED_KEYS = ("spec_version", "username", "compose")

    GITHUB_USERNAME_RE = re.compile(
        r"""
        (?!.{40})       # max length 39 characters
        [a-z\d]+        # starts with letter/digit
        (?:-[a-z\d]+)*  # hyphens must be followed by letters/digits
        """,
        re.IGNORECASE | re.ASCII | re.VERBOSE,
    )

    SCOPE_STACK_RE = re.compile(
        r"""
        (?!.{40})       # max length 39 characters
        [a-z\d]+        # only letters/digits
        """,
        re.IGNORECASE | re.ASCII | re.VERBOSE,
    )

    RESERVED_GROUP_SCOPES = (
        "compose",
        "docker",
        "git",
        "nftables",
        "ssh",
        "system",
        "stacks",
        "stack",
        "custom",
        "karo",
    )

    def err(key: str, msg: str) -> None:
        raise ConfigError(f"Invalid config: '{key}' {msg}")

    def check_lowercase(key: str, value: str) -> None:
        if value != value.lower():
            err(key, "must be lower case")

    def check_username(key: str, username: str) -> None:
        if GITHUB_USERNAME_RE.fullmatch(username) is None:
            err(
                key,
                "may only contain alphanumeric characters or single hyphens, "
                "and cannot begin or end with a hyphen",
            )

    def check_scope_stack(key: str, value: str) -> None:
        if SCOPE_STACK_RE.fullmatch(value) is None:
            err(key, "can only use alphanumeric characters")

    def check_group_name(key: str, stack_group: str) -> None:
        p = stack_group.split("_")

        if len(p) != 2:
            err(key, "invalid stack group format (<username>_<scope>)")

        group_username, group_scope = p

        # username checks

        if group_username != config_data["username"]:
            err(
                key,
                f"stack group must use defined username '{config_data['username']}'",
            )

        check_username(key, group_username)

        # scope checks

        if not group_scope:
            err(key, "stack group scope must not be empty")

        check_scope_stack(key, group_scope)

        if group_scope in RESERVED_GROUP_SCOPES:
            err(key, "stack group cannot use reserved scope name")

    unknown_keys = set(config_data) - set(KEYS)

    if unknown_keys:
        unknown = "', '".join(sorted(unknown_keys))
        raise ConfigError(f"Invalid config: unknown keys '{unknown}'")

    for key in KEYS:
        if key not in config_data:
            if key in REQUIRED_KEYS:
                # required key not found
                err(key, "is required")

            # optional key not found
            match key:
                # set defaults for missing keys
                case "author":
                    config_data["author"] = config_data["username"]
                case "license":
                    config_data["license"] = "NOASSERTION"
            continue

        value = config_data[key]

        match key:
            case "spec_version":  # int, >= 1
                if not isinstance(value, int):
                    err(key, "must be an integer")

                if value < 1:
                    err(key, "must be >= 1")

            case "username":  # str, lower case
                if not isinstance(value, str):
                    err(key, "must be a string")

                if not value:
                    err(key, "must not be empty")

                check_username(key, value)

                check_lowercase(key, value)

            case "author":  # str
                if not isinstance(value, str):
                    err(key, "must be a string")

                if not value:
                    err(key, "is empty")

            case "license":  # str
                if not isinstance(value, str):
                    err(key, "must be a string")

                if not value:
                    err(key, "is empty")

            case "dependencies":  # list[str], lower case
                if not isinstance(value, list):
                    err(key, "must be a list")

                if not value:
                    err(key, "is empty")

                for i, dependency in enumerate(value):
                    dependency_key = f"dependencies[{i}]"

                    if not isinstance(dependency, str):
                        err(dependency_key, "must be a string")

                    if not dependency:
                        err(dependency_key, "is empty")

                    check_username(dependency_key, dependency)

                    check_lowercase(dependency_key, dependency)

            case "compose":  # dict[str, list[str]], all lower case
                if not isinstance(value, dict):
                    err(key, "must be a TOML table")

                if not value:
                    err(key, "must not be empty")

                for group, stacks in value.items():
                    group_key = f"compose.{group}"

                    check_lowercase(group_key, group)

                    if not isinstance(stacks, list):
                        err(group_key, "must be a list")

                    if not stacks:
                        err(group_key, "is empty")

                    check_group_name(group_key, group)

                    for i, stack in enumerate(stacks):
                        stack_key = group_key + f"[{i}]"

                        if not isinstance(stack, str):
                            err(stack_key, "must be a string")

                        if not stack:
                            err(stack_key, "is empty")

                        check_scope_stack(stack_key, stack)

                        check_lowercase(stack_key, stack)
