# GitHub Workflows

This directory contains GitHub Actions workflows for automated CI/CD processes.

## Workflows

### `build-and-push.yml`

Builds and pushes Docker images for the backend and frontend services to GitHub Container Registry (GHCR).

#### Triggers

- **Push** to `main` or `develop` branches when files in `backend/`, `frontend/`, or workflow files change
- **Pull Request** to `main` branch when files in `backend/`, `frontend/`, or workflow files change

#### Features

- **Path-based triggering**: Only builds services when their respective directories change
- **Conditional building**: Uses `dorny/paths-filter` to detect changes and only build affected services
- **Multi-arch support**: Uses Docker Buildx for advanced build features
- **Caching**: Implements GitHub Actions cache for faster builds
- **Proper tagging**: Creates tags based on branch, PR, SHA, and latest for default branch

#### Image Names

Images are pushed to:
- `ghcr.io/<owner>/<repo>-backend`
- `ghcr.io/<owner>/<repo>-frontend`

#### Tags

- `main` - Latest stable version
- `develop` - Development version
- `pr-<number>` - Pull request builds
- `<branch>-<sha>` - Branch with commit SHA
- `latest` - Only on default branch

#### Required Permissions

The workflow requires the following permissions:
- `contents: read` - To checkout repository
- `packages: write` - To push to GitHub Container Registry

#### Usage

The workflow runs automatically on pushes and pull requests. To manually trigger:

1. Go to Actions tab in GitHub
2. Select "Build and Push Docker Images"
3. Click "Run workflow"

#### Prerequisites

- Dockerfiles must exist in `backend/` and `frontend/` directories
- Repository must have GitHub Container Registry enabled
- No additional secrets required (uses `GITHUB_TOKEN`)