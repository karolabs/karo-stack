---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/form
---

# Templates

While Docker Compose files offer considerable flexibility, this can also introduce ambiguity, confusion, and inconsistency.
To avoid these issues, and to better facilitate collaboration and maintenance, the following principles should be adhered to:

- **Verbose** - Stacks must be more explicit in their definitions, avoiding ambiguity.
  Preferring long-form syntax, and absolute paths.
  To create more clearly and safely defined stacks.

- **Precise** - Every line in the compose file must have a understood purpose.
  No keeping definitions just because the author of original of the compose file included them.
  And any non-standard definitions should be explained in more detail.

- **Standardised** - Stacks must follow a consistent ordering and structure of definitions.
  Reducing potential errors, and making work across different stacks much more seamless.

## Example stack

Also see the Docker Compose reference guides for
[services](https://docs.docker.com/reference/compose-file/services/),
[networks](https://docs.docker.com/reference/compose-file/networks/),
[volumes](https://docs.docker.com/reference/compose-file/volumes/),
and [secrets](https://docs.docker.com/reference/compose-file/secrets/).

<!-- REUSE-IgnoreStart -->

``` yaml+jinja { title="karo-compose/templates/example_group/foobar/compose.yml.j2" }
# SPDX-FileCopyrightText: © <year> <author>
#
# SPDX-License-Identifier: <license>

---

name: foobar
services:

  foobar:
    image: {{ stack_vars.foobar.image }}:{{ stack_vars.foobar.version }}
    container_name: foobar
    restart: {{ karo_compose_restart_policy }}
    # security
    # user: 1000:1000
    # tty: false
    # stdin_open: false
    # read_only: true
    # security_opt:
    #   - no-new-privileges:true
    # tmpfs:
    #   - /tmp:rw,noexec,nosuid,nodev
    # cap_drop:
    #   - ALL
    networks:
      - egress_foobar
      - frontend
    volumes:
      - type: bind
        source: /srv/docker/example_group/foobar/config.json
        target: /app/config.json
        read_only: true
      - type: volume
        source: foobar_data
        target: /app/data
    labels:
      - traefik.enable=true
      - traefik.http.routers.foobar.rule=Host(`{{ stack_vars.foobar.domain }}`)
      - traefik.http.services.foobar.loadbalancer.server.port=1234
{% if stack_vars.foobar.forward_auth_enabled %}
      # forward auth
      - traefik.http.routers.foobar.middlewares=tinyauth
      - tinyauth.apps.foobar.config.domain={{ stack_vars.foobar.domain }}
      - tinyauth.apps.foobar.oauth.groups={{ karo_compose_oidc_admin_group }}
{% endif %}
    environment:
      - LOG_LEVEL={{ stack_vars.foobar.log_level }}
      - TZ={{ karo_compose_timezone }}
      - FOOBAR_API_TOKEN_FILE=/run/secrets/foobar_api_token
    secrets:
      - foobar_api_token

networks:
  egress_foobar:
    name: egress_foobar
    driver: bridge
    internal: false
  frontend:
    external: true

volumes:
  foobar_data:
    name: foobar_data

secrets:
  foobar_api_token:
    file: {{ karo_compose_secrets_path }}/foobar_api_token
```

<!-- REUSE-IgnoreEnd -->

??? info "Naming conventions"

    - Volume names: `<container name>_<volume use>` (e.g. foobar_data, foobar_cache)

    - Network names: `<network use>_<container name>` (e.g. frontend_foobar, backend_foobar, egress_foobar)

    - Use lowercase letters and underscores only.

??? info "Port mappings"

    Its unlikely you'll need to map any ports.
    As most stacks only use web traffic (ports 80 & 443), which will always handled by the reverse proxy.
    However, there may be times when new port mappings are required.

    Use the following short syntax for port mappings:

    ``` html { .no-copy }
    ports:
      - "<HOST>:<CONTAINER>/<PROTOCOL>"
    ```

    Ensure you **always specify the protocol**.
    And for stacks that need both UDP and TCP traffic on the same port, you'll need to map the same port twice for both protocols.

??? info "UID 1000"

    Unlike rootful Docker, when a rootless Docker container uses UID 1000, it's not using the host user 1000 (karo).
    Instead, the user running the Docker daemon (dockeruser) has been assigned a [subordinate user ID range](https://docs.docker.com/engine/security/userns-remap/) (dockeruser:165536:65536).
    So user 1000 for the container is one of these unprivileged subordinate users.

    ``` sh { .no-copy }
    $ stat /home/dockeruser/.local/share/docker/volumes/pocketid_data/_data
    Access: (0755/drwxr-xr-x)  Uid: (166535/ UNKNOWN)   Gid: (166535/ UNKNOWN)
    ```

    Sometimes you'll need the UID of files created by a container to match that of the host user.
    Setting the UID to be `0` will achieve this effect.
    As UID 0 is mapped to the UID of the host user running the rootless daemon.
