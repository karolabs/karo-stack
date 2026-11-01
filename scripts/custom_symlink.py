# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

import os
import sys
from pathlib import Path  # https://docs.python.org/3/library/pathlib.html

DEFAULTS_DIR = Path("roles/karo/compose/defaults/main")
TEMPLATES_DIR = Path("roles/karo/compose/templates")

def main() -> None:
    # handle existing compose role symlinks
    remove_broken_symlinks(DEFAULTS_DIR)
    remove_broken_symlinks(TEMPLATES_DIR)

    # symlink inventory
    if Path("inventory/compose").is_dir():
        symlink_custom_repo(Path("inventory"))

    # define karo-custom repos list
    repos = list_repos()

    # symlink repos
    if repos:
        print(f"repos: {[repo.name for repo in repos]}")
        for repo in repos:
            symlink_custom_repo(repo)
    else:
        print("no karo-custom repos found")

def remove_broken_symlinks(directory: Path) -> None:
    for path in directory.iterdir():
        # check for broken symlink
        if path.is_symlink() and not path.exists():
            print(f"removing broken link: {path}")
            path.unlink()

def list_repos() -> list[Path]:
    # list directory paths inside ./repos
    repos = []
    for path in Path("repos").iterdir():
        if path.is_dir():
            repos.append(path) # repos/karolabs
    return sorted(repos)

def create_symlink(link_file: Path, target: Path) -> None:
    if not link_file.exists():
        relative_target = Path(os.path.relpath(path=target, start=link_file.parent))
        link_file.symlink_to(relative_target)

def symlink_custom_repo(repo_dir: Path) -> None:
    compose_dir = repo_dir / "compose" # repos/karolabs/compose

    # symlink yaml files into compose role defaults
    for yaml_file in compose_dir.rglob("*.yml"):
        # e.g. yaml_file is "repos/karolabs/compose/karolabs_core/traefik/stack.yml"
        match yaml_file.name:
            case "images.yml":
                link_file = DEFAULTS_DIR / f"{repo_dir.name}.images.yml"

            case "group.yml":
                group_dir = yaml_file.parent # ../karolabs_core
                link_file = DEFAULTS_DIR / f"{group_dir.name}.group.yml"

            case "stack.yml":
                stack_dir = yaml_file.parent # ../traefik
                group_dir = stack_dir.parent # ../karolabs_core
                link_file = DEFAULTS_DIR / f"{group_dir.name}_{stack_dir.name}.stack.yml"

            case _:
                print(f"ignored unknown yaml file: {yaml_file}")
                continue

        create_symlink(link_file, target=yaml_file)

    # symlink group dirs into compose role templates
    for group_dir in compose_dir.iterdir():
        if group_dir.is_dir():
            # e.g. group_dir is "repos/karolabs/compose/karolabs_core"
            link_file = TEMPLATES_DIR / group_dir.name
            create_symlink(link_file, target=group_dir)

main()
sys.exit(0)
