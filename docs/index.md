---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/house
title: Home
---

# karo-stack

**A minimal toolkit for building a declarative Linux homeserver**

[![Latest release](https://img.shields.io/github/v/release/karolabs/karo-stack?display_name=tag&cacheSeconds=7200&label=Release)](https://github.com/karolabs/karo-stack/releases)
[![License](https://img.shields.io/badge/License-AGPL--3.0-B461B3)](https://github.com/karolabs/karo-stack/blob/main/LICENSE)

:simple-debian: :simple-git: :simple-ansible: :simple-docker:

---

## About

The karo-stack aims to provide a middle ground for managing a self-hosted setup.
Somewhere between manually installing Docker on a bare bones server.
And using an all-encompassing, abstracted solution like Proxmox or Unraid.
Manual methods often become problematic when maintaining things long-term.
Whereas the alternative is likely overkill for the needs of most users.

This is why the karo-stack exists, built to a philosophy of six intrinsic principals:

<div class="grid cards" style="grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));" markdown>

- :lucide-book-text: **Declarative**
- :lucide-circle-check: **Unambiguous**
- :lucide-lock-keyhole: **Secure**
- :lucide-bolt: **Extensible**
- :lucide-tree-pine: **Stable**
- :lucide-code-xml: **Open-source**

</div>

!!! info "TL;DR"

    The karo-stack enables users to reliably and
    efficiently deploy a personalised self-hosted homeserver.

    Starting with an automated installation of Debian Linux.
    The server configuration tracked in git.
    Sensitive information encrypted inside a vault.
    Tasks are orchestrated using
    [Ansible](https://docs.ansible.com/projects/ansible/latest/getting_started/introduction.html)
    with idempotent behaviour.
    And self-hosted Docker stacks run securely as a rootless user.

## Setup overview

1. Install Debian with a preseed file
2. Setup the karo-stack git repo
3. Run the Ansible playbook
4. Add custom provided Docker stacks
5. Start your configured services

Read the [requirements page](setup/requirements.md).
