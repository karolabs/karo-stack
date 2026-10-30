---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/square-asterisk
---

# Secrets

Stacks sometimes need to handle sensitive data (e.g. API tokens, OIDC secrets, passwords, etc).
This data should not be stored inside a Docker Compose file, in plain text.
Instead, the data should be passed directly into a container during its creation.
This is done by using [Docker secrets](https://docs.docker.com/reference/compose-file/secrets/).

## Secrets lifecycle

### Variable to secrets file

1.  For users, there is no functional difference between declaring a sensitive value, versus declaring a normal one.
    Both are variables declared inside their encrypted Ansible vault.
    Though secrets are always defined under a nested dictionary named `secrets`.

    ``` yaml+jinja { .no-copy title="(karo-inventory)/host_vars/homeserver/vault.yml" hl_lines="7-8" }
    example_group_foobar_enabled: true

    example_group_foobar_stack:
      foobar:
        domain: "foobar.{{ karo_compose_root_domain }}"
        log_level: info
        secrets:
          api_token: "xP5SDH57+zn4hR804VFN#p=="
    ```

2.  When `just compose up` is run, the Ansible playbook creates a file for each secret.
    These new files only exist temporarily, and are stored within a tmpfs filesystem (in system memory).
    When ready, the Ansible playbook always removes the files, even if a task fails.

    ``` yaml+jinja { .no-copy title="/run/user/1001/karo-compose/example_group/foobar/foobar_api_token" }
    xP5SDH57+zn4hR804VFN#p==
    ```

### Docker Compose stack

1.  The compose template is rendered, and
    the [top-level secrets definition](https://docs.docker.com/reference/compose-file/secrets/#:~:text=The%20top%2Dlevel%20secrets%20declaration)
    inside the compose file defines a new Docker secret.
    Its value is set based on the contents of a secrets file.

    ``` yaml+jinja { .no-copy title="(karo-custom)/compose/example_group/foobar/compose.yml.j2" hl_lines="11-13" }
    --8<-- "docs/snippets.md:compose_secrets_example"
    ```

    !!! info "Secrets file path"

        The path to the secrets file is defined per stack.
        And the variable `karo_compose_secrets_path` is updated dynamically for use in the compose template.

2.  Having defined a Docker secret, the service must explicitly inherit it.
    Adding the Docker secret to the service means Docker will create the secrets file inside the container
    (this similar to a bind mount).
    These secrets files are found at `/run/secrets` inside the container's filesystem.

    ``` yaml+jinja { .no-copy title="(karo-custom)/compose/example_group/foobar/compose.yml.j2" hl_lines="8-9" }
    --8<-- "docs/snippets.md:compose_secrets_example"
    ```

3.  The secret can finally be used by the service.
    This is normally done with an environment variable,
    pointing to the path of the secrets file created inside the container.

    !!! warning "Service support for Docker secrets"

        The service used must support setting an environment variable or config value to the contents of a file.

    ``` yaml+jinja { .no-copy title="(karo-custom)/compose/example_group/foobar/compose.yml.j2" hl_lines="6-7" }
    --8<-- "docs/snippets.md:compose_secrets_example"
    ```
