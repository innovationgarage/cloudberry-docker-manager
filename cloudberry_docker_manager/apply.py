import docker

def apply(config):
    client = docker.from_env()

    existing_containers = {c.name: c for c in client.containers.list(all=True, filters={'label': 'cloudberry-docker-manager'})}

    intended_containers = {"cloudberry-docker-manager-%s" % spec['uuid']: spec
                           for spec in config.config['data']['config']['containers']}

    for name, spec in intended_containers.items():
        if name not in existing_containers:
            client.containers.run(
                spec.get('image', 'cloudberry-lede-openwisp-docker:latest'),
                detach=True,
                cap_add=['NET_ADMIN'],
                ports={'%s/%s' % (port.get("guest"),port.get("proto", "tcp")): port.get("host", port.get("guest"))
                       for port in spec.get('ports', [1194])},
                labels=["cloudberry-docker-manager"],
                name=name,
                environment={
                    'OPENWISP_URL': config.base_url,
                    'OPENWISP_UUID': spec['uuid'],
                    'OPENWISP_KEY': spec['key']
                })

    for name, container in existing_containers.items():
        if name not in intended_containers:
            container.stop()
            container.remove()
        if container.status != 'running':
            container.start()
