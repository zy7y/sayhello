# centos 执行 sh deploy.sh
docker build -t sayhello .
docker run -d --name sayhello-bottle -p 8000:80 sayhello
