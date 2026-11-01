#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

from pathlib import Path # https://docs.python.org/3/library/pathlib.html

DEFAULTS_DIR = Path("roles/karo/compose/defaults/main")
TEMPLATES_DIR = Path("roles/karo/compose/templates")

def main() -> None:
    # handle existing compose role symlinks
    remove_broken_symlinks(DEFAULTS_DIR)
    remove_broken_symlinks(TEMPLATES_DIR)

    # symlink inventory
    if Path("inventory/compose").exists():
        symlink_defaults("inventory")
        symlink_templates("inventory")

    # define karo-custom repos list
    repos = list_repos()

    # symlink repos
    if repos:
        print(f"repos: {repos}")
        for repo in repos:
            symlink_defaults(repo)
            symlink_templates(repo)
    else:
        print("no karo-custom repos found")
    return

def remove_broken_symlinks(directory: Path) -> None:
    for path in directory.iterdir():
        # check for broken symlink
        if path.is_symlink() and not path.exists():
            print(f"removing broken link: {path}")
            path.unlink()
    return

def list_repos() -> list[str]:
    # define directories list for ./repos
    repos = []
    for path in Path("repos").iterdir():
        if path.is_dir():
            repos.append(path.name) # karolabs
    return sorted(repos)

def symlink_defaults(repo: Path) -> None:

    repo_path = "inventory" if repo == "inventory" else f"repos/{repo}"

    # loop karo-custom repo yaml files
    for defaults_file in Path(f"{repo_path}/compose").rglob("*.yml"):
        # e.g. defaults_file is "repos/karolabs/compose/karolabs_core/traefik/stack.yml"

        # symlink defaults files
        match defaults_file.name:
            case "images.yml":
                link = Path(f"{DEFAULTS_DIR}/{repo}.images.yml")
                target = Path(f"../../../../../{defaults_file}")
                if not link.exists():
                    link.symlink_to(target)

            case "group.yml":
                group_name = defaults_file.parent.name # karolabs_core
                link = Path(f"{DEFAULTS_DIR}/{group_name}.group.yml")
                target = Path(f"../../../../../{defaults_file}")
                if not link.exists():
                    link.symlink_to(target)

            case "stack.yml":
                stack_name = defaults_file.parent.parts[-1] # traefik
                group_name = defaults_file.parent.parts[-2] # karolabs_core
                link = Path(f"{DEFAULTS_DIR}/{group_name}_{stack_name}.stack.yml")
                target = Path(f"../../../../../{defaults_file}")
                if not link.exists():
                    link.symlink_to(target)

            case _:
                print(f"ignored unknown yaml file: {defaults_file}")
    return

def symlink_templates(repo: Path) -> None:

    repo_path = "inventory" if repo == "inventory" else f"repos/{repo}"

    # symlink group dirs
    for group_dir in Path(f"{repo_path}/compose").iterdir():
        if group_dir.is_dir():
            # e.g. group_dir is "repos/karolabs/compose/karolabs_core"
            link = Path(f"{TEMPLATES_DIR}/{group_dir.name}")
            target = Path(f"../../../../{group_dir}")
            if not link.exists():
                link.symlink_to(target)
    return

main()
exit(0)
