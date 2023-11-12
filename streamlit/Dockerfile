FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip3 install -r req.txt

HEALTHCHECK CMD curl --fail http://localhost:4000/_stcore/health

ENTRYPOINT ["streamlit", "run", "Deicide.py", "--server.port=4000", "--server.address=0.0.0.0", "--server.enableCORS=false"]