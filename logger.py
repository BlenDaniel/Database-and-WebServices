#!usr/bin/env python3
from os import access
from apachelogs import LogParser
import numpy as np
import matplotlib.pyplot as plt


remote_hosts = []
counts = []

def parser_1(line):
    parser_1 = LogParser(
        "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    try:
        entry = parser_1.parse(line.rstrip()+'\n')
        host = entry.remote_host
        if host in remote_hosts:
            counts[remote_hosts.index(host)] += 1
        else:
            remote_hosts.append(host)
            counts.append(1)
        return True
    except Exception:
        return False


def parser_2(line):
    parser_2 = LogParser("%h %l %u %t \"%r\" %>s %b")
    try:
        entry = parser_2.parse(line.rstrip()+'\n')
        host = entry.remote_host
        if host in remote_hosts:
            counts[remote_hosts.index(host)] += 1
        else:
            remote_hosts.append(host)
            counts.append(1)
        return True
    except Exception:
        return False

def plotGraph():
    with open("access_log.txt") as file:
        for line in file:
            parser = parser_1(line)
            if(parser == False):
                parser_2(line)

    fig = plt.figure()

    plt.title('The Log')
    plt.xlabel('IPs')
    plt.ylabel('Traffic')
    plt.bar(remote_hosts, counts, width=0.4)
    plt.savefig('Access_Log_Plot.pdf')


plotGraph()

