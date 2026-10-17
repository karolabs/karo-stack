---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/archive-restore
---

# Restore setup configuration

If you've previously...

- Created your `karo-inventory` repo
- Configured your vault
- Run different Docker stacks

You can use this guide to quickly restore your previous setup.

Note that this guide only aims to restore your karo-stack configuration.
It does not restore Docker volumes, personal data,
or any previous system changes you might have made.

## Restore steps

!!! info "Installing Debian"

    You should still follow the normal guide first, from [Requirements](../setup/requirements.md) to Installation.

With Debian installed, follow these commands to quickly restore your setup:

--8<-- "docs/snippets.md:copying_commands"

--8<-- "docs/snippets.md:pipx_install"

--8<-- "docs/snippets.md:git_clone"

--8<-- "docs/snippets.md:just_password"

!!! info "New updates"

    If some time has passed since last running your setup. Then please consult the project's [release notes](https://github.com/karolabs/karo-stack/releases), and ensure there are no new breaking changes.

``` sh
just install all homeserver
```
