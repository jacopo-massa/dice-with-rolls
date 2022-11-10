FROM python:3.8-alpine
ADD . /dice_service
WORKDIR /dice_service
RUN pip3 install -r requirements.txt
EXPOSE 5002
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
