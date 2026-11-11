# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging
from datetime import date
from importlib import resources
from pathlib import Path
from string import Template

log = logging.getLogger(__name__)


def review_repo(config: dict, apply_mode: bool) -> None:
    """Certify repository's contents against defined config values."""

    COMPOSE_DIR = Path("compose")
    TEMPLATES_DIR = resources.files("karo_custom") / "templates"

    TEMPLATE_NAMES = {
        "images": "images.yml",
        "group": "group.yml",
        "compose": "compose.yml.j2",
        "stack": "stack.yml",
    }

    # read bundled templates (e.g. "images.yml": <template text>)
    TEMPLATES = {
        filename: (TEMPLATES_DIR / filename).read_text(encoding="utf-8")
        for _, filename in TEMPLATE_NAMES.items()
    }

    # define common template variables
    TEMPLATE_VARS = {
        "year": date.today().year,
        "author": config["author"],
        "license": config["license"],
        "username": config["username"],
    }

    def format_group_stacks(group: str) -> str:
        stacks = config["compose"][group]
        # generate list of stacks as string
        return "\n".join(f"  - {stack}" for stack in stacks)

    def write_file(file: Path) -> None:
        file_vars = TEMPLATE_VARS.copy()

        # define path dependant variables
        if file.name in (TEMPLATE_NAMES["compose"], TEMPLATE_NAMES["stack"]):
            # stack dir
            file_vars.update(
                group=file.parent.parent.name,
                stack=file.parent.name,
            )
        elif file.name == TEMPLATE_NAMES["group"]:
            # group dir
            file_vars.update(
                group=file.parent.name,
                stack_list=format_group_stacks(file.parent.name),
            )

        # create file from related template
        file.write_text(
            data=Template(TEMPLATES[file.name]).substitute(file_vars),
            encoding="utf-8",
        )

    def action_dir(directory: Path) -> None:
        # check for existing dir
        if directory.is_dir():
            log.debug(f"Found directory '{directory}'")

        # create new directory
        elif apply_mode:
            directory.mkdir()
            log.info(f"Created directory '{directory}'")

        else:
            log.warning(f"Missing directory '{directory}'")

    def action_file(file: Path) -> None:
        # check for existing file
        if file.is_file():
            log.debug(f"Found file '{file}'")

            # update group file
            if apply_mode and file.name == TEMPLATE_NAMES["group"]:
                write_file(file)
                log.info(f"Updated file '{file}'")

        # create new file
        elif apply_mode:
            write_file(file)
            log.info(f"Created file '{file}'")

        else:
            log.warning(f"Missing file '{file}'")

    # COMPOSE/
    action_dir(COMPOSE_DIR)

    action_file(COMPOSE_DIR / TEMPLATE_NAMES["images"])

    # GROUP/
    for stack_group, stacks in config["compose"].items():
        stack_group_dir = COMPOSE_DIR / stack_group

        action_dir(stack_group_dir)

        action_file(stack_group_dir / TEMPLATE_NAMES["group"])

        # STACK/
        for stack in stacks:
            stack_dir = stack_group_dir / stack

            action_dir(stack_dir)

            action_file(stack_dir / TEMPLATE_NAMES["compose"])
            action_file(stack_dir / TEMPLATE_NAMES["stack"])
