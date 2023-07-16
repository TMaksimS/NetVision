FROM python:3.10-alpine
COPY . .
WORKDIR .
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt
CMD sleep 3 && alembic upgrade head && python3 main.py
