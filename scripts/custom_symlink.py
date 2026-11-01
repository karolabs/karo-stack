# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

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
        print(f"repos: {repos}")
        for repo in repos:
            symlink_custom_repo(Path(repo))
    else:
        print("no karo-custom repos found")

def remove_broken_symlinks(directory: Path) -> None:
    for path in directory.iterdir():
        # check for broken symlink
        if path.is_symlink() and not path.exists():
            print(f"removing broken link: {path}")
            path.unlink()

def list_repos() -> list[str]:
    # define directories list for ./repos
    repos = []
    for path in Path("repos").iterdir():
        if path.is_dir():
            repos.append(path.name) # karolabs
    return sorted(repos)

def create_symlink(link: Path, target: Path) -> None:
    if not link.exists():
        link.symlink_to(target)

def symlink_custom_repo(repo: Path) -> None:
    # inventory has a different path to other custom repos
    repo_path = repo if repo == Path("inventory") else Path(f"repos/{repo}")

    # symlink yaml files into defaults
    for yaml_file in Path(f"{repo_path}/compose").rglob("*.yml"):
        # e.g. yaml_file is "repos/karolabs/compose/karolabs_core/traefik/stack.yml"
        match yaml_file.name:
            case "images.yml":
                link = Path(f"{DEFAULTS_DIR}/{repo}.images.yml")

            case "group.yml":
                group_name = yaml_file.parent.name # karolabs_core
                link = Path(f"{DEFAULTS_DIR}/{group_name}.group.yml")

            case "stack.yml":
                stack_name = yaml_file.parent.parts[-1] # traefik
                group_name = yaml_file.parent.parts[-2] # karolabs_core
                link = Path(f"{DEFAULTS_DIR}/{group_name}_{stack_name}.stack.yml")

            case _:
                print(f"ignored unknown yaml file: {yaml_file}")
                continue

        create_symlink(link, target=Path(f"../../../../../{yaml_file}"))

    # symlink group dirs into templates
    for group_dir in Path(f"{repo_path}/compose").iterdir():
        if group_dir.is_dir():
            # e.g. group_dir is "repos/karolabs/compose/karolabs_core"
            link = Path(f"{TEMPLATES_DIR}/{group_dir.name}")
            target = Path(f"../../../../{group_dir}")
            create_symlink(link, target)

main()
sys.exit(0)
