FROM python:3.9

COPY . .

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8000

CMD ["python","main.py"]
#CMD ["gunicorn", "-w 4","-t 0", "--bind= :8000", "main:app"]