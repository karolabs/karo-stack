<!--
SPDX-FileCopyrightText: © 2026 hazzuk

SPDX-License-Identifier: AGPL-3.0-only
-->

<!-- use snippets with `--8<-- "docs/snippets.md:name"` -->

<!-- commands -->

--8<-- [start:pipx_install]
```sh
# install packages
pipx install --include-deps ansible rust-just
```
--8<-- [end:pipx_install]

--8<-- [start:git_clone]
```sh
# set github username variable
GIT_USERNAME=<username>
```

```sh
# clone the karo-stack
git clone -b main git@github.com:karolabs/karo-stack.git /srv/karo
```

```sh
# clone private karo-inventory
git clone git@github.com:${GIT_USERNAME}/karo-inventory.git /srv/karo/inventory
```
--8<-- [end:git_clone]

--8<-- [start:just_password]
```sh
# set vault password
cd /srv/karo
just password
```
--8<-- [end:just_password]

<!-- admonitions -->

--8<-- [start:copying_commands]
!!! warning "Copying commands"

    You can copy and paste commands as shown (including comments).
    Always read the commands you enter.
    And where required, change any placeholder values shown in angle brackets (e.g. `<username>`).

    Do **not** edit shell parameter expansions (e.g. `#!sh echo ${GIT_USERNAME}`), these are substituted for you.
--8<-- [end:copying_commands]

--8<-- [start:terminal_paste]
!!! tip "Terminal paste"

    Use ++ctrl+shift+v++ to paste your clipboard when using the terminal.
--8<-- [end:terminal_paste]

<!-- text -->

--8<-- [start:custom_compose_filetree]
karo-compose/
├── defaults/main/
│   └── karolabs_media/
│       ├── main.yml
│       └── jellyfin.yml
└── templates/
    └── karolabs_media/
        └── jellyfin/
            └── compose.yml.j2
--8<-- [end:custom_compose_filetree]

--8<-- [start:compose_secrets_example]
name: foobar
services:

foobar:
  container_name: foobar
  environment:
    - FOOBAR_API_TOKEN_FILE=/run/secrets/foobar_api_token
  secrets:
    - foobar_api_token

secrets:
  foobar_api_token:
    file: {{ karo_compose_secrets_path }}/foobar_api_token
--8<-- [end:compose_secrets_example]
