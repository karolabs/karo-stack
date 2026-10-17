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

-   **Docker system packages**

    ``` sh
    # upgrade docker packages
    just compose down homeserver && \
    just install docker homeserver && \ # (1)!
    just compose up homeserver
    ```

    <!-- editorconfig-checker-disable -->

    1. For safety, the `docker` role will only upgrade Docker packages when
       no containers are running.

    <!-- editorconfig-checker-enable -->

-   **Debian packages** [:lucide-external-link:](https://linuxize.com/cheatsheet/apt/)

    ??? info "unattended-upgrades"

        The Debian preseed configures
        [unattended-upgrades](https://packages.debian.org/stable/unattended-upgrades).
        Every day, it attempts to automatically install
        security patches for system packages.

    ??? warning "Upgrade Docker first"

        Docker is installed as a system package using an `apt` repository.
        Upgrading all system packages will include upgrading Docker.
        This can cause unwanted container downtime.

        Upgrade Docker first to avoid this.

    ``` sh
    # upgrade system packages
    sudo apt update && \ # (1)!
    sudo apt upgrade
    ```

    1. Refreshes the package index with the latest package versions.

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
