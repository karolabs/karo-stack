---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/user-round-plus
---

# Accounts

## GitHub account

You'll need a [GitHub account](https://github.com/signup)
to store a private git repository.

Alternatively, you can also use any other git forge like
[Codeberg](https://codeberg.org/).
Which is a non-profit, community-led effort that also provides git hosting
(but this guide assumes you're using GitHub).

Once you've created your account, you'll need to add your public SSH keys.

- Add your SSH authentication, and signing keys to your
  [account's SSH keys](https://github.com/settings/keys)

## Docker account

You'll need a [Docker account](https://app.docker.com/signup)
to download [Docker hardened images](https://www.docker.com/products/hardened-images/)
used by the karo-stack.

After creating an account, you'll need to generate a PAT (save the output for use later on).

-   Generate a [new personal access token](https://app.docker.com/settings/personal-access-tokens/create)
    - Access token description: `karo-stack`
    - Expiration date: `None`
    - Access permissions: `Repo Public Read-only`
