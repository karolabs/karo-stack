---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/file-cog
---

# Configuration file

Every karo-custom repo must have a `karo-custom.toml` configuration file.
This [TOML](https://toml.io/en/latest) file provides basic information
about a repository and its contents.
The file also acts as a source of truth for validation and changes made by the
[karo-custom-cli](https://github.com/karolabs/karo-stack/tree/main/python/karo-custom-cli)
tool.

## Example config

``` toml { title="karo-custom.toml" }
# karo-custom repository configuration file.
# See https://docs.karolabs.dev for more information.

spec_version = 1

## github username or organisation
username = "karolabs"

## spdx copyright holder, defaults to username
author = "hazzuk"

## spdx license identifier https://spdx.org/licenses
license = "AGPL-3.0-only"

## usernames of required custom repos
# dependencies = ["karolabs"]

## stack groups and related stacks
[compose]
karolabs_core = ["traefik", "pocketid"]
karolabs_media = [
  "gluetun",
  "qbittorrent",
  "prowlarr",
  "radarr",
  "sonarr",
  "jellyfin",
  "seerr",
]
karolabs_ops = [
  "dozzle",
  "godns",
  "ntfy",
  "proxy",
  "whoami",
]
```
