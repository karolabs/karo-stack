---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/bolt
---

# karo-custom

A karo-custom repo is a user created collection
of templates for custom Docker Compose stacks.
Configurable and deployed like the
rest of the karo-stack using Ansible.
While also designed to be shareable,
for use by others on their own homeserver.

## Overview

### The traditional approach

Docker services are defined by
[compose files](https://docs.docker.com/compose/intro/compose-application-model),
which offer a multitude of different configuration options.
When looking to setup a new service, it's the norm to simply use the
example compose file offered by the application's developer.
But these files are always written in slightly different ways,
often without readability or additional security hardening in mind.

Because while there is of course a specification that
sets out how compose compose files _can_ be defined.
There is no set of guidelines for
how compose files _should_ be best written.

Nor is there an easy way to share a compose setup
without also requiring others to make their own changes.
Either to the compose file, config files, or to other services
needed to integrate the stack.

The karo-stack aims to help alleviate
these common issues and improve the overall
Docker experience with the use of karo-custom repos.

### A new approach

karo-custom repos were designed to be a complimentary
system for managing Docker Compose stacks.
Where compose files become templates, which can include variables
that users can substitute with their own configuration
(instead of needing to edit a compose file directly).

``` yaml+jinja { title="Traefik compose.yml.j2 (truncated example)" }
name: traefik
services:
  traefik:
    image: {{ stack_vars.traefik.image }}
    container_name: traefik
```

Stack configuration is stored beside
the rest of the user's karo-stack config,
inside their encrypted Ansible vault.
Which Ansible uses along with the
templates to render (and then deploy) standard compose.yml files.

![karo-custom diagram](../assets/images/karo-custom_architecture_v1.excalidraw.svg)

/// caption
Custom stacks deployment
///

Users can pull from pre-existing karo-custom repos
instead of having to write every stack themselves.
This helps avoid the burden of maintenance falling
solely on the shoulders of one individual.
And what would of been many users creating
multiples of the same stack, can instead ideally be many
users working to maintain and improve one custom stack.

Those who wish to write custom stacks can
rely on a standardised Docker environment,
along with detailed documentation and helpful tooling.
All working to ease the setup process,
while also promoting long-term stability and improved security.

- :lucide-form: Templated compose files

- :lucide-file-lock: Encrypted and version controlled stack configuration

- :lucide-cog: Ansible orchestration

- :lucide-server: Standardised Docker environment

- :lucide-list-checks: Suggested compose configuration guidelines

- :lucide-bolt: Easily shareable stacks system
