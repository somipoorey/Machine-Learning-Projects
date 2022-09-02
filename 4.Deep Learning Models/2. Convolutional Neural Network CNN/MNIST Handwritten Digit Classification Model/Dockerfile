FROM python:3.8.8
COPY ./model /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python
RUN apt-get update -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]