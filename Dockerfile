FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY load_xml_to_db.py .

COPY Q9Y261.xml .

CMD [ "python", "load_xml_to_db.py" ]