---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/house
title: Home
---

<style>
    .md-typeset h1 {
        font-size: 2.925em;
        margin: 0.2em 0 0.85em;
    }
    .md-sidebar__inner {
        display: none;
    }
    .md-footer__inner:not([hidden]) {
        display: none !important;
    }
</style>

# <img class="twemoji" src="https://hazzuk.github.io/assets/karolabs/karolabs.svg"> | karo-stack

**A minimal toolkit for declaratively configuring a Linux homeserver**

[![Latest release](https://img.shields.io/github/v/release/karolabs/karo-stack?display_name=tag&cacheSeconds=7200&label=Release)](https://github.com/karolabs/karo-stack/releases)
[![License](https://img.shields.io/badge/License-AGPL--3.0-B461B3)](https://github.com/karolabs/karo-stack/blob/main/LICENSE)

:simple-debian: :simple-git: :simple-ansible: :simple-docker:

---

The karo-stack provides a middle ground between manually
handling Docker containers on a bare bones server,
and using an all-in-one platform such as Unraid or TrueNAS.
Manual setups can become increasingly difficult to maintain over time,
while larger platforms can introduce unnecessary overhead
and layers of abstraction that many setups simply don't need.
Instead, the karo-stack offers a purpose-built toolkit
for configuring a well-optimised homeserver.
It leaves the user in control of their system,
while providing structure and useful automation.

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
