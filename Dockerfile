FROM python:3.7
COPY . /sayhello
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
EXPOSE 9000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
