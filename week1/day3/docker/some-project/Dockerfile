FROM python:3.13-slim

WORKDIR /proj

COPY backend/ backend/
COPY .env .
COPY pyproject.toml .
RUN python3.13 -m venv .venv 
RUN .venv/bin/pip install -e .

ENTRYPOINT ["sh", "-c", ". .venv/bin/activate && python3.13 backend/manage.py migrate && python3.13 backend/manage.py runserver 0.0.0.0:80"] 
#CMD ["python3.13", "backend/manage.py", "runserver", "0:0:0:0:81"]
