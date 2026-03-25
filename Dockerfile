FROM python:3.11-slim

# Create directory (Optional). Bydefault WORKDIR /App
RUN mkdir /Ops

WORKDIR /Ops

RUN chdir /Ops

COPY src/ /Ops/

COPY tests/ /Ops/

COPY requirements.txt /Ops/
COPY requirements-dev.txt /Ops/

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "ops.py" ]
CMD [ “—port”, “5000” ]






