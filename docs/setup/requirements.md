---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/clipboard-check
---

# Requirements

You'll need the following before starting:

- [ ] Homeserver hardware
- [ ] Computer to configure the server
- [ ] Bootable 8 GB+ USB drive
- [ ] Registered domain name ([Cloudflare](https://www.cloudflare.com/products/registrar/) is preferred, but not required)
- [ ] Password manager (ideally with SSH agent support, i.e.
  [1Password](https://developer.1password.com/docs/ssh/agent),
  [Bitwarden](https://bitwarden.com/help/ssh-agent/),
  [KeePassXC](https://keepassxc.org/docs/#faq-ssh-agent-how))

## Recommended knowledge

Suggested (but not required) to have a basic understanding or awareness of the following topics:

- [Docker Compose](https://docs.docker.com/compose/intro/compose-application-model/)
- [Linux command-line](../usage/linux.md)
- DNS records
- IP addresses
- Port forwarding
- Git version control
- TLS certificates
- SSH keys

## Suggested server hardware

- :lucide-memory-stick: 4 GB of RAM
- :lucide-cpu: 2 CPU cores
- `x86_64`/`amd64` processor

??? info "ARM CPU support"

    While there is no reason an `ARM64`/`AArch64` processor won't work, it's not an architecture that is tested with.
    So your mileage may vary.
    If you encounter any issues, please don't hesitate to raise a
    [GitHub issue](https://github.com/karolabs/karo-stack/issues/new/choose).

??? warning "Ryzen 3000 CPU's (or older)"

    If you are using an AMD Zen 1 or Zen 2 processor, you might encounter
    [issues with the processor's power management](https://gist.github.com/dlqqq/876d74d030f80dc899fc58a244b72df0).
    After installing Debian, you can fix this by adding a kernel parameter via the GRUB boot loader.

    ``` sh
    sudo micro /etc/default/grub
    ```

    ``` ini { title="/etc/default/grub" }
    # include for amd cpu power management mitigations
    GRUB_CMDLINE_LINUX_DEFAULT="quiet processor.max_cstate=1"
    GRUB_CMDLINE_LINUX="processor.max_cstate=1"
    ```

    ``` sh
    sudo update-grub
    sudo reboot
    ```
