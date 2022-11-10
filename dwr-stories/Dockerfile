FROM python:3.8-alpine
ADD . /StoriesService
WORKDIR /StoriesService
RUN pip3 install -r requirements.txt
EXPOSE 5003
CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]