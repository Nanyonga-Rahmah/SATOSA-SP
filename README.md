# SATOSA Test Service Provider

A minimal SAML 2.0 Service Provider (SP) used for testing a local
SATOSA proxy deployment. Built with Flask and pysaml2.

## Requirements

- Python 3.11+
- `libxml2-dev`, `libxmlsec1-dev`, `libxmlsec1-openssl`, `pkg-config`
  (system packages required to build `pysaml2`)

On Debian/Ubuntu:

```sh
sudo apt-get install -y libxml2-dev libxmlsec1-dev \
    libxmlsec1-openssl pkg-config
```

## Project Structure
sp/
├── src/
│   └── sp/
│       ├── init.py
│       ├── app.py              # Flask application and routes
│       ├── config.py           # pysaml2 SP configuration
│       └── generate_metadata.py
├── certs/                      # SP signing certificate/key
├── metadata/                   # SAML metadata (SP and IdP/proxy)
├── templates/                  # Flask HTML templates
├── tests/
├── pyproject.toml
├── GNUmakefile
└── .pre-commit-config.yaml

## Setup

Clone the repository, then run:

```sh
make setup
```

This creates a virtual environment, installs the package in
editable mode with development dependencies, and installs the
pre-commit hooks.

## Running the SP

Start the Flask development server:

```sh
make run
```

The app listens on `http://localhost:8000` with the following
routes:

- `/` — home page
- `/login` — starts a SAML authentication request to the
  configured IdP/proxy
- `/metadata` — serves this SP's SAML metadata
- `/acs` — Assertion Consumer Service; receives and validates the
  SAML response

The SP expects a SATOSA proxy (or other SAML IdP) reachable at the
entity ID configured in `src/sp/app.py`. See the main `satosa`
project for the proxy setup this SP is intended to work with.

## Development

Format code:

```sh
make format
```

Lint and type-check:

```sh
make lint
```

Run tests:

```sh
make test
```

Pre-commit hooks run automatically on `git commit` and enforce
formatting, linting, and
[Conventional Commits](https://www.conventionalcommits.org/)
message style. To run all hooks manually against the full
codebase:

```sh
.venv/bin/pre-commit run --all-files
```

## Configuration

SAML settings (entity ID, endpoints, certificates, metadata
sources) are defined in `src/sp/config.py`. Certificates are
expected at `certs/sp.key` and `certs/sp.crt`, and trusted IdP/
proxy metadata is read from `metadata/`.
