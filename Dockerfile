FROM python:3.7
COPY . /app
COPY /usr/share/zoneinfo/Asia/Shanghai /usr/share/zoneinfo/Asia
WORKDIR ./app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
