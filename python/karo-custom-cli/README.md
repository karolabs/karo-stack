<!--
SPDX-FileCopyrightText: © 2025 hazzuk

SPDX-License-Identifier: AGPL-3.0-only
-->

# karo-custom-cli

Command-line interface for creating karo-custom repos.

Can be used by both brand new and existing repositories.

## Features

- Validates your `karo-custom.toml` configuration file.

- Warns when expected files are missing.

- `--apply` will create the necessary file structure defined by `karo-custom.toml`,
  and update any existing `group.yml` files.

## Install

Recommended to use `pipx`.

Simply run the install command and supply a path to this directory.

`pipx install --editable --force ./python/karo-custom-cli/`

## Usage

``` sh
# navigate to your locally cloned karo-custom git repo
cd ./projects/git/karo-custom

# see help text
karo-custom --help

# run read only checks
karo-custom

# create/update files and directories
karo-custom --apply
```
