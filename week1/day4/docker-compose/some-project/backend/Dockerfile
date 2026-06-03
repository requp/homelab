FROM python:3.13-slim AS builder
WORKDIR /proj

COPY pyproject.toml requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt

COPY src src
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels .

FROM python:3.13-slim AS runner
COPY --from=builder /proj/wheels /wheels
COPY --from=builder /proj/src /src
WORKDIR /src

RUN pip install --no-cache /wheels/* && rm -rf /wheels

CMD ["sh", "-c", "./manage.py migrate && ./manage.py runserver 0.0.0.0:8000"]

