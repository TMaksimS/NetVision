FROM python:3.10
COPY . .
WORKDIR .
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]