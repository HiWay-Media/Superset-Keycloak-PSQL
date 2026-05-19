# Changelog

All notable changes to this project will be documented in this file.

## 2026-05-19

- Added `Dockerfile.modern` to support newer Apache Superset image tags without modifying the stable `Dockerfile`.
- Updated `README.md` with build instructions for stable and modern Docker variants.
- Kept `.github/workflows/docker-publish.yml` unchanged for production image publishing.
- Added `.github/workflows/docker-publish-modern.yml` to publish a separate modern image to `ghcr.io/<owner>/<repo>-modern`.
- Fixed `.github/workflows/docker-publish-modern.yml` repo metadata step for `actions/github-script@v7` by switching to `github.rest.repos.get(...)`.