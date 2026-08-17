import os

from .base import *

DEBUG = False


allowed_hosts_env = os.environ.get("ALLOWED_HOSTS", "")

ALLOWED_HOSTS = allowed_hosts_env.split(",") if allowed_hosts_env else []


# Database
DATABASES = {
    # TODO: Add production database settings
}
