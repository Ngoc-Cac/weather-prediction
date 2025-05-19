FROM jupyter/scipy-notebook
WORKDIR /home/work

COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt
RUN rm requirements.txt