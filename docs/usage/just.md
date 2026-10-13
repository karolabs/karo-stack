---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/file-terminal
---

# just

The karo-stack uses [just](https://just.systems/man/en/),
a tool to run project-specific commands.
Each just command is called a recipe,
these recipes help simplify common commands
you'll need to run when using the project.

<!-- editorconfig-checker-disable -->

??? info "Commands vs just recipes"

    This is the main Ansible playbook command:

    - `ansible-playbook run.yml --tags install --limit "homeserver"`

    But the karo-stack uses just to
    provide a simplified way of invoking this command:

    - `just install homeserver`
      (This recipe runs the command shown above, and additional logic)

<!-- editorconfig-checker-enable -->

Recipes can be invoked from any subdirectory,
as recipes run with the working directory set
to the directory that contains the justfile.
You can use `just help` to see a full list of available recipes,
or run `just help <recipe>` to see more detailed usage information.

## System setup

### :lucide-monitor-check: `install`

Run Ansible to configure the core components of your system.

!!! example "Recipe examples"

    ``` sh { .no-copy }
    # runs the main ansible roles to setup 'homeserver'
    just install homeserver
    ```

    ``` sh { .no-copy }
    # runs the main ansible roles to setup 'proxyserver'
    just install proxyserver
    ```

### :lucide-container: `compose`

Run Ansible to deploy or remove custom Docker Compose stacks.

!!! example "Recipe examples"

    ``` sh { .no-copy }
    # setup on 'homeserver' all enabled stacks
    just compose up homeserver
    ```

    ``` sh { .no-copy }
    # setup on 'homeserver' the 'traefik' stack (if enabled)
    just compose up homeserver -s traefik
    ```

    ``` sh { .no-copy }
    # remove on 'homeserver' all enabled stacks
    just compose down homeserver
    ```

    ``` sh { .no-copy }
    # remove on 'proxyserver' the 'proxy' stack (if enabled)
    just compose down proxyserver -s proxy
    ```

    !!! note "Stack data"

        Using `just compose down` is the same as `docker compose down`,
        meaning stack data will persist.

    ``` sh { .no-copy }
    # force recreate 'pocketid' stack
    just compose recreate homeserver -s pocketid
    ```

## Ansible vault

### :lucide-file-lock: `vault`

Create or edit an Ansible vault.

!!! example "Recipe example"

    ``` sh { .no-copy }
    # create or edit an ansible vault inside 'inventory/host_vars/homeserver/vault.yml'
    just vault homeserver
    ```

### :lucide-key-square: `password`

Create or edit a temporary Ansible vault password file.

!!! example "Recipe example"

    ``` sh { .no-copy }
    # create or edit the ansible vault password file inside '/run/user/1000/karo/ansible/vault_pass'
    just password
    ```

## Custom repos

### :lucide-bolt: `custom`

Get or remove karo-custom repositories.

!!! example "Recipe example"

    ``` sh { .no-copy }
    # get karo-custom repo from github
    just custom get karolabs
    ```

    ``` sh { .no-copy }
    # remove existing karo-custom repo
    just custom remove karolabs
    ```

## Debian install

### :lucide-sprout: `preseed`

An optional preseed method,
running a Python webserver to host the Debian `preseed.cfg` file.
Making it accessible for use over a local network.

!!! example "Recipe examples"

    ``` sh { .no-copy }
    # starts a python webserver to host 'debian/server/d-i/trixie/preseed.cfg'
    just preseed server
    ```

    ``` sh { .no-copy }
    # starts a python webserver to host 'debian/desktop/d-i/trixie/preseed.cfg'
    just preseed desktop
    ```

    !!! note "When to use this recipe"

        For use by advanced users, or when testing changes to the preseed file.
        See [this guide](../setup/debian/preseed.md#automatic-setup-advanced)
        for details.
