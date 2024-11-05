# ***Backend***

# Development

To develop, you need to deploy the server using Docker-compose.
To install Docker and Docker-compose, follow [link](https://docs.docker.com/get-started/get-docker/)

You can deploy servers using the following commands:

```bash
    docker compose up -d
```

When the container starts, a script is run using migrations and collecting static files

The project uses the package manager [uv](https://docs.astral.sh/uv /)

- you can run the Python command on the server:

- bash (recommended) 
```bash
docker exec -t backend uv run [COMMAND]
```

- inside the container
```bash
uv run [COMMAND]
```

- the local environment can be deployed with the command:
    **from the backend folder**
    ```bash
        uv sync
    ```

## CI checks

- **Please perform all checks inside Docker containers** to avoid failed CI checks. Below are the commands to run the checks:


- check backend typing

   - bash (recommended) 
    ```bash
        docker exec -t backend uv run mypy .
    ```

    - inside the container
    ```bash
        uv run mypy .
    ```

- check backend linting

    - bash (recommended) 
    ```bash
        docker exec -t backend uv run ruff check .
    ```

    - inside the container
    ```bash
        uv run ruff check .
    ```

- backend testing

    - bash (recommended) 
    ```bash
        docker exec -t backend uv run pytest
    ```

    - inside the container
    ```bash
        uv run ruff pytest
    ```


## Documentation development

The [MkDocs](https://www.mkdocs.org/user-guide/configuration/) library is used to develop documentation 

- **No need to build documentation and then commit.** CI has a task set up to build and publish documentation for merge requests

- **There is no Docker container for documentation development.** You can run the documentation development server in a virtual environment. Below is the command:

    - **from the backend folder**
    ```bash
        uv run mkdocs serve
    ```