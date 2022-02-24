FROM python:latest
WORKDIR /gp/userapi
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY .venv/lib/python3.10/site-packages/pyclient.py /usr/local/lib/python3.10/site-packages
COPY mlclient.py /usr/local/lib/python3.10/site-packages
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]
