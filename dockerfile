FROM python:3.7
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["scoreboard.py"]
ENTRYPOINT ["python3"]