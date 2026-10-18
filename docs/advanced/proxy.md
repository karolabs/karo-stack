---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/waypoints
---

# VPS proxy

!!! warning

    This guide is incomplete and the setup is still experimental. Everything is subject to change without notice.

It is critical to consider the security of exposing services to the public internet. The easiest method to expose services is simply opening ports on your router. However, this makes your home network more vulnerable. And you'll have to disclose your network's public IP address. Alternatively, you can avoid opening ports by using a VPN. This way you connect directly to the server, and traffic is tunnelled when accessing services. But this can be cumbersome, and difficult for end-users to correctly utilise.

The karo-stack's solution to this issue actually involves a mix of both approaches. You'll open ports, but on a rented VPS (Virtual Private Server) instead of your home network. And your new VPS will then be directly connected to your server over a VPN connection. With this setup, inbound public traffic will be sanitised on the VPS first, before being tunnelled on towards your server.

## Proxy stack

You'll need to rent a small VPS, ideally one geographically close to you. Then after installing Debian and setting up the karo-stack on the VPS. You'll deploy the project's custom `proxy` stack.

``` mermaid
flowchart LR
  subgraph Internet
    User@{ shape: stadium }
  end

  subgraph proxyserver ["VPS (proxyserver)"]
    HAProxy
    CrowdSec
  end

  subgraph homeserver ["Homeserver (proxyclient)"]
    Traefik
  end

  User e1@===|HTTPS| HAProxy
  HAProxy --- CrowdSec
  HAProxy e2@-..-|WireGuard| Traefik

  e1@{ animation: fast }
  e2@{ animation: slow }
```

There are three parts to the proxy stack:

- **HAProxy** - A high performance reverse proxy. Routes traffic [without needing to terminate TLS](https://www.bomberbot.com/proxy/haproxy-and-server-name-indication-sni-the-definitive-guide/) connections on the VPS. And can preserve the user's IP address using the [PROXY protocol](https://www.haproxy.com/blog/use-the-proxy-protocol-to-preserve-a-clients-ip-address).

- **CrowdSec** - A crowdsourced web application firewall. Detects and blocks malicious traffic.

- **WireGuard** - A VPN protocol. Securely tunnels traffic between the VPS and homeserver.

This page outlines the steps required to setup a VPS for use as a `proxyserver` with the karo-stack.

## DNS records

Your VPS will likely have a static IPv4 address, so you won't need to use a dynamic DNS service. Instead, simply create a DNS `A` record targeting the `<vps public ipv4>`.

| Type | Name          | Target              | Comment              |
| ---- | ------------- | ------------------- | -------------------- |
| A    | `proxyserver` | `<vps public ipv4>` | vps - public traffic |

!!! tip "Internal DNS"

    If you're using an internal server DNS, it's important to also add this same record there as well. (Otherwise you can't use the hostname `proxyserver.example.com` in the following SSH commands. As your internal DNS would incorrectly resolve this as your homeserver's internal IP address.)

Any services you've previously exposed publicly (e.g. `CNAME` `jellyfin` `dyndns.example.com`), should instead now be targeted at `proxyserver.example.com`. And ports `80` and `443` should be closed on your router.

## VPS setup

Most VPS providers will simply create a pre-configured Debian server for you. As such, if you can't self-install Debian (and use the preseed file). Then you'll need to configure your new Debian VPS manually. And create the correct environment for the Ansible playbook to run in.

### Debian post-install

Connect via SSH as the `root` user:

``` sh
ssh root@proxyserver.example.com
```

Run the following commands to replicate the preseed process:

``` sh
# apply updates
apt update
apt upgrade
```

``` sh
# create karo user
adduser --comment "" karo
usermod -aG sudo karo
```

``` sh
# create karo directories
install -d -m 0775 -o karo -g karo /srv/karo
install -d -m 0775 -o karo -g karo /home/karo/.ssh
```

``` sh
# create karo authorized_keys
install -m 0644 -o karo -g karo /root/.ssh/authorized_keys /home/karo/.ssh
```

``` sh
# install packages
apt -y install \
    chrony man-db parted wireguard \
    btop curl micro rsync tree wget \
    acl pipx python3-debian python3-requests \
    ca-certificates uidmap \
    git nftables openssh-server
```

``` sh
# finish manual setup
exit
```

### Ansible vault

!!! info "Continuing setup on your homeserver"

    From this point onwards, setup of the VPS should be handled via Ansible on your homeserver.

Connect via SSH to your **homeserver**:

``` sh
ssh -A karo@homeserver.example.com
```

Use your existing vault password for Ansible:

``` sh
just password
```

Create and edit a new vault named `proxyserver`:

``` sh
just vault proxyserver
```

``` yaml { title="/srv/karo/inventory/host_vars/proxyserver/vault.yml" }
# proxyserver
#
# CONFIDENTIAL

---

# [ansible]

ansible_become_password: "" # karo user root password

# [git]

karo_git_user_email: git@example.com # github email
karo_git_user_name: username # github username
karo_git_user_signingkey: "ssh-ed25519 AAAAC3NqnC1bZEIl2..." # public signing key

# [nftables]

## ports 80 (tcp) and 443 (tcp/udp) are already accepted
# karo_nftables_accepted_tcp_ports: "" # e.g. "53, 465, 587"
# karo_nftables_accepted_udp_ports: "" # e.g. "7777, 25565"

# [ssh]

## this port will be accepted by nftables
karo_ssh_port: 4444

# [docker]

karo_docker_login_username: username # docker username
karo_docker_login_token: "dckr_pat_..." # docker personal access token

# [compose]

karo_compose_root_domain: example.com # registered domain name

karo_compose_timezone: "Europe/London" # utctime.info/timezone

## docker will start stack groups in this order
## docker will stop stack groups in reverse order
karo_compose_stack_groups:
  - karolabs_core
  - karolabs_media
  - karolabs_ops

# [custom]
```

### Ansible playbook

Update your inventory's `hosts.ini` file to include the VPS as a new host:

``` sh
micro /srv/karo/inventory/hosts.ini
```

``` ini { title="/srv/karo/inventory/hosts.ini" hl_lines="3" }
[server]
homeserver ansible_host=localhost ansible_connection=local ansible_user=karo
proxyserver ansible_host=proxyserver.example.com ansible_port=22 ansible_connection=ssh ansible_user=karo
```

Run the playbook for the VPS:

``` sh
just install all proxyserver
```

Afterwards, adjust your `hosts.ini` file to use the new SSH port `#!ini ansible_port=4444`:

``` sh
micro /srv/karo/inventory/hosts.ini
```

### Git changes

Commit your new changes:

``` sh
cd /srv/karo/inventory

git add *
git commit -m "update inventory files"
git push
```

## Stack setup

After having successfully setup your VPS, you're now ready to run the proxy stack. You can read all the necessary details about the stack's configuration on its [dedicated page](https://custom.karolabs.dev/karolabs_ops/proxy/).

!!! tip "Running the stack"

    Once you've correctly configured your vault, you can deploy the proxy stack:

    ``` sh
    just compose up proxyserver -s proxy
    ```
