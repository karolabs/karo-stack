# SPDX-FileCopyrightText: © 2025 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

# justfile, for running project-specific commands.
# See https://just.systems/man/en for more information.

set minimum-version := '1.55.0'
set default-list := true

# HELPER RECIPES
# ---

# List recipes or usage
[arg('recipe', help="Justfile recipe name (e.g. 'install', 'compose')")]
@help recipe='':
    {{ just_executable() }} {{ if recipe != "" { "--usage " + recipe } else { '' } }}

# Reusable confirmation statement
[private]
[confirm("proceed? (y/N)")]
@confirm:
    echo

hostname_usage := "Ansible managed host (e.g. 'homeserver', 'proxyserver')"

# DEBIAN INSTALL
# ---

# Host preseed.cfg
[group('Debian install')]
@preseed platform='server':
    # check user input for platform
    [ "{{platform}}" = "server" ] || [ "{{platform}}" = "desktop" ] || { echo "platform must be 'server' or 'desktop'" >&2; exit 1; }
    # check user key file exists
    [ -e "inventory/key.txt" ] || { echo "inventory/key.txt not found" >&2; exit 1; }
    # insert public ssh key into preseed file
    just insert-preseed-key "$(cat inventory/key.txt)" {{platform}}
    # run webserver
    -just host-preseed {{platform}}
    -# revert change to preseed file
    -just insert-preseed-key "<key>" {{platform}}

# Write the authorized SSH key to the Debian preseed file
[private]
@insert-preseed-key value platform:
    sed -i "s|echo '.*'|echo '{{value}}'|" debian/{{platform}}/d-i/trixie/preseed.cfg

# Run a Python HTTP server to host the preseed file
[private]
host-preseed platform:
    @echo "press 'Ctrl + C' to exit"
    -python3 -m http.server 8000 --bind 0.0.0.0 --directory ./debian/{{platform}}

# SYSTEM SETUP
# ---

# Setup a system
[group('System setup')]
[arg('role', help="Ansible role name", pattern="all|system|nftables|ssh|git|docker|micro")]
[arg('hostname', help=hostname_usage)]
@install role hostname='': check-password
    # run ansible playbook
    ansible-playbook run.yml \
        --tags "{{ if role == "all" { "install" } else { role } }},untagged" \
        --limit "{{hostname}}"

# Up/down/recreate Docker stacks
[group('System setup')]
[arg('action', help="Docker Compose command", pattern="up|down|recreate")]
[arg('hostname', help=hostname_usage)]
[arg('stack', long, short="s", help="karo-custom stack name (e.g. 'traefik', 'pocketid')")]
@compose action hostname='' stack='all': check-password
    # manage symlinks
    just custom-symlink
    # run ansible playbook
    ANSIBLE_DISPLAY_SKIPPED_HOSTS=false \
    ansible-playbook run.yml \
        --extra-vars "karo_compose_justfile_stack={{stack}}" \
        --extra-vars '{"karo_compose_recreate_enabled":{{ if action == "recreate" { "true" } else { "false" } }}}' \
        --tags "compose,untagged,{{action}}" \
        --limit "{{hostname}}"

# ANSIBLE VAULT
# ---

password_file := "/run/user/1000/karo/ansible/vault_pass"

# Manage a vault
[group('Ansible vault')]
[arg('hostname', help=hostname_usage)]
vault hostname:
    #!/usr/bin/env bash
    set -euo pipefail
    # check password file exists
    if [ -e "{{password_file}}" ]; then
        # check vault file exists
        export vault="inventory/host_vars/{{hostname}}/vault.yml"; echo $vault
        if [ -e "$vault" ]; then
            # edit existing vault
            ansible-vault edit "$vault"
        else
            # create new vault
            ansible-vault create "$vault"
        fi
    else
        echo "{{password_file}} not found, run 'just password'." >&2; exit 1;
    fi

# Create Ansible vault password file when missing
[private]
@check-password:
    [ -e "{{password_file}}" ] || micro -backup false -mkparents true "{{password_file}}"

# Set password file
[group('Ansible vault')]
@password:
    micro -backup false -mkparents true "{{password_file}}"

# WIREGUARD
# ---

# Generate key pair
[private]
wireguard:
    @priv="$(wg genkey)"; \
    pub="$(wg pubkey <<<"$priv")"; \
    printf 'Private key: %s\n' "$priv"; \
    printf 'Public key: %s\n' "$pub"

# CUSTOM REPOS
# ---

custom_repo_name := "karo-custom"

# Get/remove custom repo
[group('Custom repos')]
[arg('action', help="karo-custom repo command", pattern="get|remove")]
[arg('username', help="karo-custom repo username (e.g. 'karolabs', 'hazzuk')")]
@custom action username:
    just custom-{{action}} {{lowercase(username)}}

# Get remote karo-custom repo
[private]
custom-get username:
    #!/usr/bin/env bash
    set -euo pipefail
    printf "repo: github.com/{{username}}/{{custom_repo_name}}\n\n"
    # clone karo-custom git repo
    git clone git@github.com:{{username}}/{{custom_repo_name}}.git repos/{{username}}
    # check repo dir not empty
    if [ -z "$(find repos/{{username}}/karo-compose -mindepth 1 -maxdepth 1)" ]; then
        exit 0
    else
        # manage symlinks
        just custom-symlink
        # list stack groups for username
        printf "\nnew stack groups:\n"
        ls -1 roles/karo/compose/templates | grep {{username}} | awk '{print "- " $0}'
    fi

# Remove a karo-custom repo
[private]
@custom-remove username:
    printf "removing repos/{{username}}\n"
    # check repo dir exists
    test -d "repos/{{username}}"
    # confirm removal
    just confirm
    # remove repo dir
    rm -rf "repos/{{username}}"
    # manage symlinks
    just custom-symlink

# Manage symbolic links for custom files
[private]
custom-symlink:
    #!/usr/bin/env bash
    set -euo pipefail
    # clear existing symlinks
    find roles/karo/compose/defaults/main/ -mindepth 1 -maxdepth 1 ! -name "main.yml" -delete
    find roles/karo/compose/templates/ -mindepth 1 -maxdepth 1 ! -name ".gitkeep" -delete
    # check repos dir not empty
    if [ -z "$(find repos -mindepth 1 -maxdepth 1)" ]; then
        exit 0
    else
        # symlink custom files
        ln -sr repos/*/karo-compose/defaults/main/*/ roles/karo/compose/defaults/main/
        ln -sr repos/*/karo-compose/templates/*/ roles/karo/compose/templates/
    fi
    # check inventory for compose dir
    if [ -d inventory/karo-compose ]; then
        # symlink custom files from inventory
        ln -sr inventory/karo-compose/defaults/main/*/ roles/karo/compose/defaults/main/
        ln -sr inventory/karo-compose/templates/*/ roles/karo/compose/templates/
    fi
