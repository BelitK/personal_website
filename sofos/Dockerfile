FROM python:3.9

COPY . .

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8000

CMD ["gunicorn", "-w 4", "--bind= :8000", "main:app"]