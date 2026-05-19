# Changelog

All notable changes to this project will be documented in this file.

## 2026-05-19

- Added `Dockerfile.modern` to support newer Apache Superset image tags without modifying the stable `Dockerfile`.
- Updated `README.md` with build instructions for stable and modern Docker variants.
- Kept `.github/workflows/docker-publish.yml` unchanged for production image publishing.
- Added `.github/workflows/docker-publish-modern.yml` to publish a separate modern image to `ghcr.io/<owner>/<repo>-modern`.
- Fixed `.github/workflows/docker-publish-modern.yml` repo metadata step for `actions/github-script@v7` by switching to `github.rest.repos.get(...)`.
- Fixed `Dockerfile.modern` dependency install to reduce CI build failures (`Flask-OpenID==1.3.0` and `psycopg2-binary==2.9.9`).
- Set modern default base image to Apache Superset `6.1.0` in both `Dockerfile.modern` and `docker-publish-modern.yml`.
- Added `.github/workflows/docker-test-modern.yml` to run a Docker Compose smoke test for the modern image (`Dockerfile.modern`) with Postgres + Superset health check.