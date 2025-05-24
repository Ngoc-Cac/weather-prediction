FROM python:3.12-slim-bullseye
WORKDIR /home/work

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --progress-bar off --no-cache-dir -r requirements.txt\
    --extra-index-url https://download.pytorch.org/whl/cpu
RUN rm requirements.txt

CMD ["tail", "-f", "/dev/null"]