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

<div class="grid cards" markdown>

-   :lucide-book-text:{ .lg .middle } **Declarative**

    ---

    Unambiguous configuration using
    [Ansible](https://docs.ansible.com/projects/ansible/latest/getting_started/introduction.html).

-   :lucide-bolt:{ .lg .middle } **Extensible**

    ---

    Reusable [custom](custom/index.md) Docker compose stacks.

-   :lucide-face-slightly-smiling:{ .lg .middle } **Not by AI**

    ---

    Developed [by humans](about/index.md) with great care.

-   :lucide-code-xml:{ .lg .middle } **Open Source**

    ---

    Licensed under AGPLv3, code on
    [GitHub](https://github.com/karolabs/karo-stack).

    <!-- The karo-stack is licensed under the AGPLv3 and is available on
    [GitHub](https://github.com/karolabs/karo-stack). -->

</div>

!!! info "TL;DR - Configure a personalised homeserver for self-hosting"

    - Semi-automated Debian Linux installation.
    - Declarative system configuration orchestrated using
      Ansible with idempotent behaviour.
    - Configuration tracked inside a private git repository.
    - Sensitive data encrypted using an Ansible vault file.
    - Dedicated rootless Docker environment for running containers.
    - Templated Docker Compose stacks that can be reused and shared.

## Setup overview

1. Install Debian using a preseed file (bare metal or VM)
2. Setup the karo-stack git repo
3. Run the Ansible playbook
4. Add custom Docker Compose stacks
5. Start your configured services

Read the [requirements page](setup/requirements.md).
