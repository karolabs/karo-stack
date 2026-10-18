---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/variable
---

# Defaults

Compose files for the karo-stack are created as
[Ansible templates](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_templating.html).
Templates are helpful as they can utilise variables,
which get replaced with their values when the template is deployed.
This removes the need for users to modify any compose file directly.
Instead, users simply define variables inside their vault,
which later become a part of the rendered template.

However, users aren't expected to define every possible variable,
and they also need to know the variable names to use.
Hence a defaults file, which contains all available variables,
with default values to be overridden where needed.

## Defaults files

To add a stack (e.g. 'foobar') to your karo-custom repo, you'd need to create two defaults files.

-   `main.yml` (internal variables, primarily for the deployment order of stacks)

    ``` yaml+jinja { .no-copy title="karo-compose/defaults/main/example_group/main.yml" }
    # docker will start stacks in this order
    # docker will stop stacks in reverse order
    example_group_stacks:
      - foobar
    ```

-   `foobar.yml` (stack variables, for users to override)

    !!! info "Stack variables"

        All variables created for a stack need to be added to the stack's defaults file.

        Common variables include `image`, `version`, `domain` and `log_level`.

    ``` yaml+jinja { .no-copy title="karo-compose/defaults/main/example_group/foobar.yml" }
    example_group_foobar_enabled: false

    example_group_foobar_stack_defaults:
      foobar:
        image: docker.io/foobarorg/foobar
        version: v1.0.0@sha256:100689790a0a0ea43ca45997e0450bc26aeb5308375b41c84dfc4f
        domain: "foobar.{{ karo_compose_root_domain }}"
        log_level: info # debug, info, warn, error
        forward_auth_enabled: false
        secrets:
          api_token: ""
    ```

## Variable precedence

Stack dictionary variables are declared twice:

- In the defaults file, with a `_defaults` suffix (e.g. `example_group_foobar_stack_defaults`)
- In the inventory's Ansible vault file (e.g. `example_group_foobar_stack`)

Ansible merges these together, so that user values override default values.
The resulting variable of the combined dictionaries is named `stack_vars`.

!!! abstract "Extended explanation"

    Unlike simple variables (e.g. `name: value`),
    [dictionary variables](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html#dictionary-variables)
    aren't combined when two of the same name exist between the defaults file and user's inventory.
    Instead, one will take
    [precedence](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable),
    replacing the other.

    === "Two dictionaries (same name)"

        When there are two dictionaries defined with the same name
        (e.g. one in a defaults file, another by the user),
        they are not combined.
        Instead, it's all or nothing, one automatically takes precedence.

        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(10rem,1fr));" markdown>

        ``` yaml { .no-copy title="Defaults dict" }
        test:
          stuff:
            one: "1"
            two: "2"
        ```

        ``` yaml { .no-copy title="Inventory dict" }
        test:
          stuff:
            two: "222"
        ```

        ``` yaml { .no-copy title="Resulting dict" }
        test:
          stuff:
            two: "222"
        ```

        </div>

    === "Two dictionaries (different names, manually combined)"

        Uniquely named dictionaries ensures neither is overwritten.
        Both can then be manually merged to create a new combined dictionary.
        Here, the preference is for the inventory dictionary to take precedence.

        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(10rem,1fr));" markdown>

        ``` yaml { .no-copy title="Defaults dict" }
        test_defaults:
          stuff:
            one: "1"
            two: "2"
        ```

        ``` yaml { .no-copy title="Inventory dict" }
        test:
          stuff:
            two: "222"
        ```

        ``` yaml { .no-copy title="Combined dict" }
        test_new:
          stuff:
            one: "1"
            two: "222"
        ```

        </div>

    ---

    As such, any stack dictionary variable defined in a
    defaults file **must** be appended with the phrase `_defaults`.
    This allows for two dictionaries to be defined.
    One by the user, and another by the defaults.

    They're later found and merged by the Ansible playbook.
    The resulting variable of the combined dictionaries is named `stack_vars`.
    Which can be used inside any templates file (e.g. `compose.yml.j2`).
