import logging

from superset.security import SupersetSecurityManager


logger = logging.getLogger(__name__)


class KeycloakSecurityManager(SupersetSecurityManager):
    """Security manager for Superset 6.x using FAB's AUTH_OAUTH (Authlib).

    Userinfo is extracted from the Keycloak OIDC userinfo endpoint and roles
    are taken from the access token (realm_access.roles + resource_access roles)
    so they can be mapped via AUTH_ROLES_MAPPING in superset_config.
    """

    def oauth_user_info(self, provider, response=None):
        if provider != "keycloak":
            return {}

        remote_app = self.appbuilder.sm.oauth_remotes[provider]
        userinfo = remote_app.userinfo()

        roles = []
        try:
            token = response or {}
            access_token = token.get("access_token")
            if access_token:
                import jwt

                claims = jwt.decode(
                    access_token, options={"verify_signature": False}
                )
                roles = list(claims.get("realm_access", {}).get("roles", []))
                for client_roles in claims.get("resource_access", {}).values():
                    roles.extend(client_roles.get("roles", []))
        except Exception:
            logger.exception("Failed to extract Keycloak roles from token")

        return {
            "username": userinfo.get("preferred_username") or userinfo.get("email"),
            "email": userinfo.get("email"),
            "first_name": userinfo.get("given_name", ""),
            "last_name": userinfo.get("family_name", ""),
            "role_keys": roles,
        }
