FROM python3.7
COPY . /sayhello
EXPOSE 9000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
