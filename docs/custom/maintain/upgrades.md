---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/circle-fading-arrow-up
---

# Container updates

Version updates for containers should be performed on
a regularly occurring basis, with security updates
being applied promptly.

!!! tip "Test environment"

    Container updates should be tested before being deployed.
    It is recommended to create a karo-stack test environment inside a
    virtual machine. This avoid the need to test updates
    with your live environment.

=== ":lucide-file-pen: Manual updates"

    **Select new image version**

    1. Review software release notes (take notice of any breaking changes).
    2. Pick a recent stable version (stability is preferred over brand new releases).
    3. Find and copy the associated image SHA256 digest.
    4. Update the Docker image variable inside `compose/images.yml`.

=== ":lucide-pencil-sparkles: Semi-automatic updates"

    New versions of container image tags/digests can be fetched and
    applied automatically to values inside `compose/images.yml`
    using a pre-existing GitHub Actions workflow.

    This workflow was developed by the project specifically
    for updating karo-custom Docker images. It uses
    [Updatecli](https://github.com/updatecli/updatecli)
    (a tool similar to Renovate or Dependabot) and data
    defined in YAML files to find new Docker image versions,
    and subsequently create pull requests for each change.

    ??? info "`dhi.io` authentication"

        If you want to update Docker Hardened images, you'll need to create two
        [GitHub Actions secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets):

        - `DOCKERHUB_USERNAME`
        - `DOCKERHUB_TOKEN`

    !!! tip "Allow Actions to create PRs"

        Inside your GitHub repository, you must enable the following setting:

        :octicons-gear-16: Settings →
        :octicons-triangle-circle-16: Actions →
        General → Workflow permissions

        ":lucide-square-check: Allow GitHub Actions to create and approve pull requests"

    **Workflow file**

    1. Create a new GitHub Actions workflow at `.github/workflows/updatecli.yml`.

    2. Copy and paste the contents of this
       [existing workflow](https://github.com/karolabs/updatecli/blob/main/.github/workflows/updatecli-caller.yml).

    3. Update the following variables:

        ``` yaml { .no-copy }
        github-branch: dev # (1)!
        github-pr-label: Kind/Update # (2)!
        ```

        1. Required, the git branch to work on
        2. Label added to pull requests

    **Updatecli files**

    1. For each Docker image, create a values file, e.g. `updatecli/values.d/images/cetusguard.yml`.

    2. Define the contents of each file:

        ``` yaml { title="cetusguard.yml" }
        # An `updatecli` values file, for specifying generic values.
        # See https://updatecli.io for more information.

        image:
          repository: docker.io/hectorm/cetusguard #(1)!
          # tag_regex: '^v([0-9]+\.[0-9]+\.[0-9]+)$' (2)
          # semver:
          #   pattern: '*' (3)
          #   strict: true (4)
          pr_markdown: | # (5)!
            [Releases](https://custom.karolabs.dev/karolabs_core/traefik/)
        ```

        1. Required, container image repository
        2. Regular expression extracting the version from each tag
           (default regex matches 'v1.0.0')
        3. Semantic versioning constraint (e.g. '>=2.0.0') -
           [Syntax guide](https://github.com/Masterminds/semver#checking-version-constraints)
        4. Enforce strict semantic versioning rules when parsing versions
           (e.g. 1.2 is dropped instead of being read as 1.2.0)
        5. Extra markdown included in pull requests

    The workflow will automatically run daily (or on demand) and create pull requests to be merged.

**Test updated images**

1. Recreate the relevant stack and monitor Docker logs.
2. Test the general functionality of the software.
3. If necessary, make changes to the compose templates.
