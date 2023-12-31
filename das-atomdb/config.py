import os


def load_env():
    environments = {
        "dasmongodbname": "DAS_MONGODB_NAME",
        "dasmongodbport": "DAS_MONGODB_PORT",
        "dasmongodbhostname": "DAS_MONGODB_HOSTNAME",
        "dasmongodbusername": "DAS_MONGODB_USERNAME",
        "dasmongodbpassword": "DAS_MONGODB_PASSWORD",
        "dasredishostname": "DAS_REDIS_HOSTNAME",
        "dasredisport": "DAS_REDIS_PORT",
        "dasredispassword": "DAS_REDIS_PASSWORD",
        "dasredisusername": "DAS_REDIS_USERNAME",
        "dasmongodbtlscafile": "DAS_MONGODB_TLS_CA_FILE",
        "dasuserediscluster": "DAS_USE_REDIS_CLUSTER",
        "dasusecachednodes": "DAS_USE_CACHED_NODES",
        "dasusecachedlinktypes": "DAS_USE_CACHED_LINK_TYPES",
        "dasusecachednodetypes": "DAS_USE_CACHED_NODE_TYPES",
    }

    for key, value in environments.items():
        secret = f"/var/openfaas/secrets/{key}"
        if os.path.exists(secret):
            with open(secret) as f:
                os.environ[value] = f.readline().strip()
        else:
            env_value = os.environ.get(key, None)
            os.environ[value] = env_value if isinstance(env_value, str) else ""


load_env()
