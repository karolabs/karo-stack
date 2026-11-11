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
                file_vars = TEMPLATE_VARS

                # define path dependant variables
                match file.name:
                    # stack dir
                    case "compose.yml.j2" | "stack.yml":
                        file_vars["group"] = file.parent.parent.name
                        file_vars["stack"] = file.parent.name
                    # group dir
                    case "group.yml":
                        file_vars["group"] = file.parent.name

                # create file from related template
                file.write_text(
                    data=Template(TEMPLATES[file.name]).substitute(file_vars),
                    encoding="utf-8",
                )
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
