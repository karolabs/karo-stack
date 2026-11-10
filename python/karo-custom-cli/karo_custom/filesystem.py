# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging
from pathlib import Path

log = logging.getLogger(__name__)


def review_repo(config: dict, apply_mode: bool) -> None:
    """Certify repository's contents against defined config values."""

    COMPOSE_DIR = Path("compose")

    IMAGES_FILE = Path(COMPOSE_DIR / "images.yml")
    GROUP_FILE = "{path}/group.yml"
    COMPOSE_FILE = "{path}/compose.yml.j2"
    STACK_FILE = "{path}/stack.yml"

    def action_dir(dir: Path) -> None:
        if dir.is_dir():
            log.debug(f"Found directory '{dir}'")
        else:
            if apply_mode:
                dir.mkdir()
                log.info(f"Created directory '{dir}'")
            else:
                log.warning(f"Missing directory '{dir}'")

    def action_file(file: Path) -> None:
        if file.is_file():
            log.debug(f"Found file '{file}'")
        else:
            if apply_mode:
                log.info(f"Creating file '{file}'")
                file.touch()
            else:
                log.warning(f"Missing file '{file}'")

    # COMPOSE/
    action_dir(COMPOSE_DIR)

    action_file(IMAGES_FILE)

    # GROUP/
    for stack_group, stacks in config["compose"].items():
        stack_group_dir = Path(COMPOSE_DIR / stack_group)

        action_dir(stack_group_dir)

        action_file(Path(GROUP_FILE.format(path=stack_group_dir)))

        # STACK/
        for stack in stacks:
            stack_dir = Path(stack_group_dir / stack)

            action_dir(stack_dir)

            action_file(Path(COMPOSE_FILE.format(path=stack_dir)))
            action_file(Path(STACK_FILE.format(path=stack_dir)))
