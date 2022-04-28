From ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip libpcap-dev

RUN pip install -U pip setuptools
RUN pip install boofuzz pcapy-ng impacket

CMD ["sleep", "10000"]
