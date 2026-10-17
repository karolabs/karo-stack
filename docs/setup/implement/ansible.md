---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/cog
---

# Ansible playbook

Having installed Debian, cloned the `karo-stack`,
and setup your `karo-inventory` repo.
It is now time to run the Ansible playbook.

The playbook is separated into different Ansible roles
(`system`, `nftables`, `ssh`, `git`, `docker`, and `compose`).
Each of which is responsible for configuring a specific part of the system.
These roles are mostly run together, currently grouped under two
[main tasks](https://github.com/karolabs/karo-stack/blob/main/run.yml).
One manages Docker Compose stacks, the other manages the remaining system setup.

## System roles

-   Run the playbook's main system configuration roles:

    ``` sh
    # run ansible system roles
    cd /srv/karo
    just install all homeserver
    ```

In short, this will enable the nftables firewall, make minor system changes,
tighten SSH security, adjust the git configuration,
and install rootless Docker for `dockeruser`.

??? question "Why Ansible?"

    The magic of Ansible lies in its declarative nature.
    Unlike a shell script, the playbook doesn't detail how to perform its tasks.
    Instead, it specifies the desired state of the system.
    Which Ansible then determines what actions (if any)
    are required for the system to reach that state.

    This is what leads to Ansible's idempotent behaviour.
    And is why Ansible is such a powerful tool for managing a homeserver.
    Simply put it's very good at knowing when it's doesn't have to anything at all.

    You can safely **try this for yourself** by running
    `just install all homeserver` a second time.
    As you'll see, rather than repeating every action again.
    Ansible checks that each part of the system already matches its desired state.
    And skips anything that doesn't need changing.

## Compose role

Having finished installing your new system, and configuring your initial karo-stack setup.
You can now look to deploy Docker Compose stacks.

Management of official, personal or third-party stacks is done through using karo-custom repos.

See the [Custom](../../custom/index.md) section for more details.
