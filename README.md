<!--
SPDX-FileCopyrightText: © 2025 hazzuk

SPDX-License-Identifier: AGPL-3.0-only
-->

<div align="center">

# karo-stack

**A minimal toolkit for building a declarative Linux homeserver**

[![Latest release](https://img.shields.io/github/v/release/karolabs/karo-stack?display_name=tag&cacheSeconds=7200&label=latest)](https://github.com/karolabs/karo-stack/releases)
[![License](https://img.shields.io/badge/license-AGPL--3.0-B461B3)](https://github.com/karolabs/karo-stack/blob/main/LICENSE)
[![Prek](https://github.com/karolabs/karo-stack/actions/workflows/prek.yml/badge.svg?branch=main)](https://github.com/karolabs/karo-stack/actions/workflows/prek.yml)
[![REUSE status](https://api.reuse.software/badge/github.com/karolabs/karo-stack)](https://api.reuse.software/info/github.com/karolabs/karo-stack)
[![Hits-of-Code](https://hitsofcode.com/github/karolabs/karo-stack)](https://hitsofcode.com/github/karolabs/karo-stack/view)

[![Developed by Humans, Not by AI](https://hazzuk.github.io/assets/not-by-ai/dev.svg)](https://notbyai.fyi/)

<picture>
    <img src="https://hazzuk.github.io/assets/karo-stack/header.png" alt="Connecting to a karo-stack homeserver using SSH">
</picture>

</div>

## About

The karo-stack enables users to reliably
and efficiently deploy a personalised homeserver.

Platforms such as Proxmox, Unraid and TrueNAS offer powerful,
comprehensive solutions, but that breadth can also bring unnecessary overhead
and layers of abstraction that many setups simply don't need.
The karo-stack takes a smaller approach,
as a purpose-built self-hosting solution.
It assists with installing a lightweight Debian Linux operating system,
then further configuration is applied declaratively
using Ansible and Git. This includes creating a dedicated
'rootless' Docker environment to run services more securely.

Prior experience with these underlying technologies isn't required,
although a basic understanding of self-hosting with Docker is recommended.
The project includes both detailed documentation
and a set of simplified, project-specific commands.
Together, these help guide users through homeserver setup
and ongoing maintenance, streamlining common tasks into straightforward,
repeatable processes.

It also provides an extensible system for community-maintained
Docker Compose stacks. Each one is built around a standardised environment
and robust set of guidelines. These are used to promote compatibility
between stacks and across different karo-stack homeservers.
For users, this means they can easily deploy numerous templated stacks,
configurable to an individual's needs,
without having to directly modify Compose files.

The project is completely free and open-source software,
written with careful consideration and long-term stability in mind.
It is a deliberately minimal and opinionated toolkit,
built to provide a focused set of practical features.
It takes care of the fundamentals needed for a well-optimised homeserver,
while preserving a user's sovereignty over their system.

## Documentation

Learn more about the project at [docs.karolabs.dev](https://docs.karolabs.dev/).

## Repositories

- **karo-stack** - Core server configuration (Debian preseed and Ansible playbook)

- [karo-custom](https://github.com/karolabs/karo-custom) - Official custom stacks (Docker Compose stacks)

- [karo-cli](https://github.com/karolabs/karo-cli) - Tool for generating and linting karo-custom setups

## Copyright & License

Copyright © hazzuk. Licensed AGPL-3.0-only.
