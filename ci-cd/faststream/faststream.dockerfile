FROM python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_VERSION=0.6.17
WORKDIR /app
RUN pip install "uv==$UV_VERSION"


COPY pyproject.toml uv.lock ./
RUN uv --native-tls pip install --no-cache --system -r pyproject.toml --trusted-host pypi.org --trusted-host files.pythonhosted.org

COPY ./src/faststream ./faststream
WORKDIR /app/faststream

ENTRYPOINT ["faststream", "run", "--reload", "main:app"]