FROM python:3.8
WORKDIR /content-prospector
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
COPY config/ .
CMD [ "python3", "./scraper.py" ]