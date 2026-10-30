---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/file-lock
---

# Ansible vault

Configuration of the Ansible playbook is primarily done through variables.
And as these variables sometimes contain sensitive data (e.g. a Cloudflare API token),
we use [Ansible vault](https://docs.ansible.com/projects/ansible/latest/cli/ansible-vault.html)
to encrypt the file storing all your homeserver's configuration.
Aptly named `vault.yml`.

## Password setup

Before creating the vault, you'll need a strong password to encrypt it with.

-   Generate a 96 character vault password (save the output to your password manager):

    ``` sh
    # generate vault password
    openssl rand -hex 48
    ```

Once you've saved the password,
you will also need to write it to a temporary file on the system.
This way, Ansible can access it without prompting,
when encrypting and decrypting your vault file.

-   Apply your new vault password (this command will open a text editor):

    --8<-- "docs/snippets.md:just_password"

??? question "Isn't writing the password to a plaintext file insecure?"

    The alternative approach would be Ansible prompting
    for the password each time you want to edit your vault.
    But seeing as you often need to edit the vault multiple times a session,
    this quickly becomes frustrating.

    This is why we temporarily store the password
    inside a file that Ansible can read directly.
    Which on paper is a less secure method.
    However, the karo-stack has three mitigations in place to help strengthen its security.
    First, the file you write to is shredded after every logout.
    Second, the text editor micro explicitly has backups disabled when handling this file.
    And third, the file itself is stored on a tmpfs filesystem (in system memory).

??? question "What's the `just` command?"

    The karo-stack uses just, a tool to run project-specific commands.

    For more information on using commands created for the project,
    see the documentation's [just usage](../../usage/just.md) page.

## Create your vault

With the password set, you can now create an Ansible vault file encrypted by your password.

-   Create and edit your vault:

    ``` sh
    # create ansible vault
    cd /srv/karo
    just vault homeserver
    ```

    (Copy the example below into your vault, and edit any values that require changes)

    <div class="grid" markdown>

    !!! info "Commented lines"

        Commented out variables are additional settings that are optional.

    --8<-- "docs/snippets.md:terminal_paste"

    </div>

    ``` yaml { title="/srv/karo/inventory/host_vars/homeserver/vault.yml" }
    # homeserver
    #
    # CONFIDENTIAL

    ---

    # [ansible]

    ansible_become_password: "" # karo user root password

    # [git]

    karo_git_user_email: github@example.com # github email
    karo_git_user_name: username # github username
    karo_git_user_signingkey: "ssh-ed25519 AAAAC3NqnC1bZEIl2..." # public signing key

    # [nftables]

    ## ports 80 (tcp) and 443 (tcp/udp) are already accepted
    # karo_nftables_accepted_tcp_ports: "" # e.g. "53, 465, 587"
    # karo_nftables_accepted_udp_ports: "" # e.g. "7777, 25565"

    # [ssh]

    ## this port will automatically be accepted by nftables
    # karo_ssh_port: 22

    # [docker]

    karo_docker_login_username: username # docker username
    karo_docker_login_token: "dckr_pat_..." # docker personal access token

    # [micro]

    ## use terminal clipboard for copy/paste
    # karo_micro_terminal_clipboard_enabled: true(1)

    # [compose]

    karo_compose_root_domain: example.com # registered domain name

    karo_compose_timezone: "Europe/London" # utctime.info/timezone

    ## docker will start stack groups in this order
    ## docker will stop stack groups in reverse order
    # karo_compose_stack_groups:
    #   - example_group

    # [custom]
    ```

    1.  Disable this if your terminal doesn't support OSC 52.

        See Micro's
        [copypaste documentation](https://github.com/micro-editor/micro/blob/master/runtime/help/copypaste.md)
        for more details.

    ??? success "Check encrypted state"

        After quitting the text editor,
        the new data is written to the vault file in an encrypted state.
        You can see this first-hand,
        by attempting to read the contents of your vault without Ansible.

        ``` sh
        # check vault encryption
        micro -readonly true /srv/karo/inventory/host_vars/homeserver/vault.yml
        ```

        You should see a long encrypted output similar to this:

        ``` yaml { .no-copy }
        $ANSIBLE_VAULT;1.1;AES256
        6538346438396339346464346163349382...
        ```
