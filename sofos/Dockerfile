FROM python:3.9

COPY . .

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8000

#CMD ["python","main.py"]
#CMD ["hypercorn", "main:app", "--bind 0.0.0.0:8000"]
CMD ["gunicorn","-w 1", "--timeout=0", "--bind= :8000", "main:app"]