FROM python:3.10.2

LABEL Khaos Research Group <khaos.uma.es>

RUN apt-get update && apt-get install -y

RUN pip install \
    typer \
    pandas \
    pyvis 
     
WORKDIR /usr/local/src/
COPY . /usr/local/src/

ENTRYPOINT ["python", "fidelityPlot.py"]
