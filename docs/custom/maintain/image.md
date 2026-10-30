---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/snowflake
---

# Image format

The container's version is controlled by the Docker image URI value:

=== "Format"

    ``` c { .no-copy title="compose example" }
    services:
      foobar:
        image: <registry>/<project>/<image>:<tag>@<digest>
    ```

=== "Template file"

    ``` yaml+jinja { .no-copy title="compose.yml.j2" }
    services:
      foobar:
        image: {{ stack_vars.foobar.image }}
    ```

=== "Result"

    ``` yaml { .no-copy title="compose.yml" }
    services:
      foobar:
        image: docker.io/foobarorg/foobar:v1.0.0@sha256:100689790a0a0ea43ca45997e0450bc26aeb5308375b41c84dfc4f2475937ab
    ```

It's common for both `<registry>` and `<digest>` to go unused when defining an image URI.
However, for greater clarity and stronger security, both should always be set.

## Registry

Specifying an image registry avoids ambiguity (normally `docker.io` or `ghcr.io`):

``` yaml { .no-copy title="images.yml (defaults file)" }
example_foobar_image: docker.io/foobarorg/foobar
```

## Digest

The image digest is the most important security mechanism when pulling images.
While tags are mutable, meaning the same tag can be later changed to another image.
Digests are immutable, as they are unique and unchangeable.
Guaranteeing you'll always pull the exact same image.

While it's not necessary to add a tag when using a digest, it's still helpful to use both.
The digest is the secure cryptographic identifier.
Whereas the tag provides a human readable version number:

``` yaml { .no-copy title="images.yml (defaults file)" }
example_foobar_image: docker.io/foobarorg/foobar:v1.0.0@sha256:100689790a0a0ea43ca45997e0450bc26aeb5308375b41c84dfc4f2475937ab
```
