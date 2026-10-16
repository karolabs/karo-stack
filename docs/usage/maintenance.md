---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/engine
---

# Maintenance

It's important to keep your server up to date and secure. This page lists
the relevant commands to update the different parts of your system.

## System upgrades

-   **Debian packages** [:lucide-external-link:](https://linuxize.com/cheatsheet/apt/)

    ``` sh
    # update package index
    sudo apt update

    # upgrade installed packages
    sudo apt upgrade
    ```

    !!! note

        A system [reboot](linux.md?h=reboot#system) is normally recommended after a new kernel is installed.

-   **Python packages**

    ``` sh
    # upgrade ansible and just
    pipx upgrade-all
    ```

## karo-stack upgrades

??? tip "karo-stack release notifications"

    Get notified about new karo-stack releases:

    1.  Go to [github.com/karolabs/karo-stack](https://github.com/karolabs/karo-stack)

    2.  Click on ':octicons-eye-16: Watch'

        - Select 'Custom'

        - Select 'Releases'

        - Select 'Apply'

    3.  Repeat this for [github.com/karolabs/karo-custom](https://github.com/karolabs/karo-custom) (recommended)

!!! warning "Breaking changes"

    Make sure to read the karo-stack's
    [release notes](https://github.com/karolabs/karo-stack/releases)
    first. And check for any breaking changes before upgrading.

    It's also recommended to stop any stack's you're currently running with
    `just compose down homeserver`.

=== "Latest"

    ``` sh
    # upgrade karo-stack to latest
    cd /srv/karo
    git pull origin main
    ```

=== "Specific version"

    ``` bash
    # set karo-stack version
    KAROSTACK_VERSION=v3.0.0
    ```

    ``` sh
    # checkout karo-stack version
    cd /srv/karo
    git fetch origin tag ${KAROSTACK_VERSION}
    git checkout ${KAROSTACK_VERSION}
    ```
