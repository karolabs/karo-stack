---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/folder-tree
---

# Repo structure

=== ":lucide-bolt: karo-custom (public repo)"

    A karo-custom repo is a dedicated public git repository for custom stacks.

    ``` text { .no-copy title="Repo example" }
    karo-custom/
    ├── compose/...
    ├── LICENSE
    └── README.md
    ```

    1. [Create a new public git repo](https://github.com/new)
        named `karo-custom` on GitHub

        - Visibility: :octicons-repo-16: Public
        - Readme: On
        - `No .gitignore`
        - [Choose a license](https://choosealicense.com/)
        (e.g. 'GNU General Public License v3.0' or 'MIT License')

    1. Clone your new repo to wherever you wish to work on it

        - To your PC, cloning it manually using git
        - To your karo-stack homeserver `just custom get <GITHUB USERNAME>`

=== ":lucide-backpack: karo-inventory (private repo)"

    You can also create private custom stacks inside
    your existing karo-inventory repository.

    ``` text { .no-copy title="Repo example" }
    karo-inventory/
    ├── compose/...
    ├── host_vars/...
    └── hosts.ini
    ```

!!! tip "karo-cli"

    To help you quickly generate the required structure,
    and lint your custom repo.
    You can use the [karo-cli](https://github.com/karolabs/karo-cli) tool.

## Example layout

Files for custom stacks are symbolically linked
to the inside of the karo-stack's Ansible playbook.
Because of this, custom stacks must follow a very specific structure.

=== "Stack group(s)"

    ``` c { .no-copy hl_lines="3" }
    --8<-- "docs/snippets.md:custom_compose_filetree"
    ```

    ??? info "Stack group rules"

        - **Must** be at least one stack group.

        - **Must** be named `<username>_<scope>`.

            Username:

            - GitHub username or organisation name that owns the public repository.
            - `inventory` when creating files inside your karo-inventory repo.

            Scope:

            - Avoid using the following words:

                - [Ansible role names](https://github.com/karolabs/karo-stack/tree/main/roles/karo) (e.g. `compose` or `system`)
                - `stack` or `stacks`
                - `custom`
                - `karo`
                - `inventory`

=== "Defaults files"

    ``` c { .no-copy hl_lines="2 4 9" }
    --8<-- "docs/snippets.md:custom_compose_filetree"
    ```

=== "Template file(s)"

    ``` c { .no-copy hl_lines="7" }
    --8<-- "docs/snippets.md:custom_compose_filetree"
    ```

    ??? info "Template rules"

        - **Must** end with a `.j2` file extension (Jinja).

        - You can create multiple template files for each stack.

            === "Template files"

                ``` c { .no-copy }
                compose/
                └── karolabs_ops/
                    └── godns/
                        ├── compose.yml.j2
                        └── config.json.j2
                ```

            === "Rendered files"

                ``` c { .no-copy }
                srv/
                └── docker/
                    └── karolabs_ops/
                        └── godns/
                            ├── compose.yml
                            └── config.json
                ```

=== "Documentation files"

    ``` c { .no-copy hl_lines="5 8" }
    --8<-- "docs/snippets.md:custom_compose_filetree"
    ```
