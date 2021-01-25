## CEKIT About
A Container image creation tool. Referece [CEKit](https://docs.cekit.io/en/latest/index.html)

## Installation instructions

### Fedora 29+

```shell
dnf install cekit
```

### Other systems

```shell
# Prepare virtual environment
python3 -m venv .env
source .env/bin/activate

# Install CEKit
pip install --upgrade pip
pip install -U cekit

cekit --help
```

Note

In this case you may need to add ~/.local/bin/ directory to your $PATH environment variable to be able to run the cekit command.

## Build an image

Use build engine podman

```shell
cekit build podman
podman images
```
