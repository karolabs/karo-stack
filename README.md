<!--
SPDX-FileCopyrightText: © 2025 hazzuk

SPDX-License-Identifier: AGPL-3.0-only
-->

<div align="center">

# karo-stack

**A minimal toolkit for configuring a declarative Linux homeserver**

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
and efficiently configure a personalised homeserver.

Platforms such as Proxmox, Unraid and TrueNAS offer powerful,
comprehensive solutions, but that breadth can also bring unnecessary overhead
and layers of abstraction that many setups simply don't need.
The karo-stack takes a different approach, providing a
purpose-built self-hosting toolkit that leverages existing
software rather than introducing another all-in-one platform.
It assists with installing a lightweight Debian Linux operating system,
then further configuration is applied declaratively
using Ansible and Git. This includes setting up a dedicated
'rootless' Docker environment to run services more securely.

It also offers an extensible system for portable Docker Compose stacks.
Each stack uses variable-driven templates and can follow a shared set of
guidelines for structuring Compose files. These conventions promote
improved readability, security hardening, and long-term maintainability,
while also helping stacks remain consistent and compatible across
karo-stack homeservers. Stack configuration is managed through the same
declarative Ansible workflow, whether users deploy community-maintained
stacks or define their own privately. The templates expose configurable
options, allowing users to quickly tailor stacks to their own needs without
having to modify Compose files directly.

The project is free and open-source software,
developed with careful consideration and long-term stability in mind.
It is a deliberately minimal and opinionated toolkit,
built to provide a focused set of practical features.
It helps take care of the fundamentals needed for a well-optimised homeserver,
while preserving a user's sovereignty over their system.

## Documentation

Prior experience with Ansible or Git isn't required,
although a basic understanding of self-hosting with Docker is recommended.
The project includes both detailed documentation
and a set of simplified, project-specific commands.
Together, these help guide users through homeserver setup
and ongoing maintenance, streamlining common tasks into straightforward,
repeatable processes.

Learn more about the project at [docs.karolabs.dev](https://docs.karolabs.dev/).

## Repositories

- **karo-stack** - Core server configuration (Debian preseed and Ansible playbook)

- [karo-custom](https://github.com/karolabs/karo-custom) - Official custom stacks (Docker Compose stacks)

- [karo-cli](https://github.com/karolabs/karo-cli) - Tool for generating and linting karo-custom setups

## Copyright & License

Copyright © hazzuk. Licensed AGPL-3.0-only.
