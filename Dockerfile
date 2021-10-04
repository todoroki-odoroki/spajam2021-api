FROM python:3.9-slim as dev
ENV PYTHONUNBUFFERED=1

WORKDIR /app

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# copy poetry file
COPY poetry.lock pyproject.toml ./

# install packages
RUN pip install poetry && \
  poetry config virtualenvs.in-project true && \
  poetry install --no-dev

COPY . ./

CMD poetry run uvicorn --host=0.0.0.0 app.main:app
# if migration is needed
# CMD poetry run alembic upgrade head && \
#     poetry run uvicorn --host=0.0.0.0 app.main:app
