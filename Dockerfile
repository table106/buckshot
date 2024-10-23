FROM python:3

WORKDIR /buckshot

COPY . .

ENV THREE="actuallytheres3"
ENV TEST="test time"

CMD [ "python", "./main.py" ]