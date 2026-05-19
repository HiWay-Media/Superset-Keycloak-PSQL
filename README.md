# Superset-Keycloak-PSQL

Superset-Keycloak is a Docker repository that provides a setup for running Apache Superset with Keycloak as the authentication and authorization provider. This integration allows you to secure your Superset instance using Keycloak's robust identity and access management capabilities.

## Description

This repository contains Docker and configuration files necessary to deploy Superset with Keycloak. It enables you to authenticate users through Keycloak and manage access to Superset's features and resources based on Keycloak roles and permissions.

## Features

- Integration of Apache Superset with Keycloak for authentication and authorization.
- Centralized user management and access control using Keycloak.
- Seamless login and Single Sign-On (SSO) experience for users.


## Prerequisites

Before running the Superset-Keycloak setup, ensure that you have the following installed on your system:

- Docker
- Keycloak

## Access Superset:

- Open your browser and navigate to http://localhost:8088 to access Superset.
- You will be redirected to the Keycloak login page, where you can authenticate with your Keycloak credentials.
- After successful authentication, you will be redirected back to Superset.

For more detailed instructions and advanced configurations, please refer to the documentation.

## Docker build options

This repository now provides two Dockerfile variants:

- `Dockerfile`: current stable setup (unchanged).
- `Dockerfile.modern`: updated setup for newer Superset image tags.

Build the stable image:

```bash
docker build -f Dockerfile -t superset-keycloak:stable .
```

Build the updated image (default tag: `latest`):

```bash
docker build -f Dockerfile.modern -t superset-keycloak:modern .
```

To pin a specific Superset version in the updated Dockerfile:

```bash
docker build -f Dockerfile.modern \
	--build-arg SUPERSET_TAG=4.1.2 \
	-t superset-keycloak:modern-4.1.2 .
```

## GitHub Actions publish

Production image publish remains unchanged via [docker-publish.yml](.github/workflows/docker-publish.yml), triggered by tags matching `v*`.

- Production image path: `ghcr.io/<owner>/<repo>`.

Modern image publish is fully isolated in [docker-publish-modern.yml](.github/workflows/docker-publish-modern.yml):

- Push tag `modern-v1.2.3` to publish modern image tags `1.2.3` and `latest`.
- Or run the workflow manually (`workflow_dispatch`) and set `superset_tag` to pin the base Apache Superset image.
- Modern image path: `ghcr.io/<owner>/<repo>-modern`.

Published image base:

```bash
ghcr.io/<owner>/<repo>
ghcr.io/<owner>/<repo>-modern
```

## Contributions
Contributions to the Superset-Keycloak repository are welcome! If you find any issues, have suggestions for improvements, or want to contribute enhancements, please open an issue or submit a pull request on the GitHub repository.

Please follow the existing code style and provide clear descriptions and documentation for any changes or additions.

## License
Superset-Keycloak is licensed under the MIT License.
