FROM python:3.12-alpine
WORKDIR /home/work

COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt
RUN rm requirements.txt

CMD ["tail", "-f", "/dev/null"]