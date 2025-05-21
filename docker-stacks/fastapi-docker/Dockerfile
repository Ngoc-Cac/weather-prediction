FROM python:3.12-alpine
WORKDIR /home/work

COPY ./requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt\
    --extra-index-url https://download.pytorch.org/whl/cpu
RUN rm requirements.txt

CMD ["tail", "-f", "/dev/null"]