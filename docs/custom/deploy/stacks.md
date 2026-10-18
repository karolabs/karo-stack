---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: simple/docker
---

# Custom stacks

!!! tip "Use the official karo-custom repo"

    The project maintains its own karo-custom repo:
    [karolabs/karo-custom](https://custom.karolabs.dev/){:target='_blank'}

    It provides essential core stacks
    (a reverse proxy and OIDC provider).
    Along with a handful of optional extra tools,
    and other services for a solid media server setup.

    !!! warning

        Whilst it's not a strict requirement to use the official karo-custom repo,
        it is **strongly recommended** (unless you want to build everything yourself).
        As other custom repos will likely utilise the core stacks.

        Once added, make sure to setup both core stacks first
        (Traefik and Pocket-ID).

## Deploy stacks from karo-custom repos

1. Clone a karo-custom repo (e.g. `just custom get <username>`)

1. Edit your Ansible vault (e.g. `just vault homeserver`)

    === "Format"

        - Add **all** available stack groups

            ``` yaml
            karo_compose_stack_groups:
              - <username>_<group>
              - <username>_<group>
              - <username>_<group>
            ```

        - Add desired stack variables

            ``` yaml
            <username>_<group>_<stack>_enabled: true

            <username>_<group>_<stack>_stack:
              <service>:
                <variable>: <value>
              <service>:
                <variable>: <value>
            ```

    === "Example"

        - Add **all** available stack groups

            ``` yaml
            karo_compose_stack_groups:
              - karolabs_core
              - karolabs_media
              - karolabs_ops
            ```

        - Add desired stack variables _(truncated example)_

            ``` yaml
            karolabs_media_qbittorrent_enabled: true

            karolabs_media_qbittorrent_stack:
              qbittorrent:
                webui_enabled: false
              qui:
                log_level: info
            ```

1. Deploy newly configured stacks (e.g. `just compose up homeserver`)

    ??? tip "Post-deployment steps"

        Remember to lower logging levels once services are running smoothly.
        And [commit any changes](../../usage/git.md) made to your Ansible vault.
