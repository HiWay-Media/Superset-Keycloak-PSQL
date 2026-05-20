import os
from typing import Optional


def get_env_variable(var_name: str, default: Optional[str] = None) -> str:
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        error_msg = "The environment variable {} was missing, abort...".format(var_name)
        raise EnvironmentError(error_msg)


ENABLE_PROXY_FIX = True
DASHBOARD_RBAC = True
FEATURE_FLAGS = {"DASHBOARD_RBAC": True}

#################################
#       METADATA DATABASE       #
#################################
DATABASE_DIALECT = get_env_variable("DB_DIALECT", "postgresql")
DATABASE_USER = get_env_variable("DB_USER")
DATABASE_PASSWORD = get_env_variable("DB_PASSWORD")
DATABASE_HOST = get_env_variable("DB_HOST")
DATABASE_PORT = get_env_variable("DB_PORT")
DATABASE_DB = get_env_variable("DB_NAME")

SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s?client_encoding=utf8" % (
    DATABASE_DIALECT,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_DB,
)

SECRET_KEY = get_env_variable("SECRET_KEY", "secret_key")

#---------------------------- KEYCLOAK (OAuth2 / OIDC) ----------------------------
# Modern path for Superset 6.x + FAB 4.x: AUTH_OAUTH with Authlib.
# Replaces the legacy flask-oidc / Flask-OpenID stack (incompatible with Flask 3).
OIDC_ENABLE = get_env_variable("OIDC_ENABLE", "False")

if OIDC_ENABLE == "True":
    from flask_appbuilder.security.manager import AUTH_OAUTH
    from keycloak_security_manager_modern import KeycloakSecurityManager

    AUTH_TYPE = AUTH_OAUTH
    CUSTOM_SECURITY_MANAGER = KeycloakSecurityManager

    AUTH_USER_REGISTRATION = True
    AUTH_USER_REGISTRATION_ROLE = get_env_variable(
        "AUTH_USER_REGISTRATION_ROLE", "Gamma"
    )
    AUTH_ROLES_SYNC_AT_LOGIN = True

    # Map Keycloak realm/client roles to Superset/FAB roles.
    # Keys are FAB role names, values are lists of Keycloak roles that grant them.
    AUTH_ROLES_MAPPING = {
        "Admin": ["superset_admin"],
        "Alpha": ["superset_alpha"],
        "Gamma": ["superset_gamma"],
        "Public": [],
    }

    KEYCLOAK_BASE_URL = get_env_variable(
        "KEYCLOAK_BASE_URL", "http://keycloak:8080"
    )
    KEYCLOAK_REALM = get_env_variable("KEYCLOAK_REALM", "master")
    KEYCLOAK_CLIENT_ID = get_env_variable("KEYCLOAK_CLIENT_ID", "superset")
    KEYCLOAK_CLIENT_SECRET = get_env_variable("KEYCLOAK_CLIENT_SECRET", "")

    _realm_url = f"{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}"

    OAUTH_PROVIDERS = [
        {
            "name": "keycloak",
            "icon": "fa-key",
            "token_key": "access_token",
            "remote_app": {
                "client_id": KEYCLOAK_CLIENT_ID,
                "client_secret": KEYCLOAK_CLIENT_SECRET,
                "server_metadata_url": f"{_realm_url}/.well-known/openid-configuration",
                "api_base_url": f"{_realm_url}/protocol/openid-connect/",
                "client_kwargs": {"scope": "openid profile email"},
                "access_token_url": f"{_realm_url}/protocol/openid-connect/token",
                "authorize_url": f"{_realm_url}/protocol/openid-connect/auth",
                "jwks_uri": f"{_realm_url}/protocol/openid-connect/certs",
            },
        }
    ]

#############################################
#       EMAIL REPORTS CONFIGURATION         #
#############################################
SMTP_ENABLE = get_env_variable("SMTP_ENABLE", "False")

if SMTP_ENABLE == "True":
    SMTP_HOST = get_env_variable("SMTP_HOST")
    SMTP_STARTTLS = True
    SMTP_SSL = False
    SMTP_USER = get_env_variable("SMTP_USER")
    SMTP_PORT = get_env_variable("SMTP_PORT")
    SMTP_PASSWORD = get_env_variable("SMTP_PASSWORD")
    SMTP_MAIL_FROM = get_env_variable("SMTP_MAIL_FROM")
