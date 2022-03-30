#!usr/bin/env python3
import re
import numpy as np
import matplotlib.pyplot as plt


def plotGraph():

    remote_hosts = []
    errors_hosts = []
    counts_host = []
    counts_errors = []

    with open("error_log.txt") as file:
        for line in file:
            m = re.findall("\[(.*?)\]", line.rstrip())
            if m and (len(m) == 4):
                host = m[3].lstrip('client')
                e_host = m[1]

                if host in remote_hosts:
                    counts_host[remote_hosts.index(host)] += 1
                else:
                    remote_hosts.append(host)
                    counts_host.append(1)
                
                if e_host in errors_hosts:
                    counts_errors[errors_hosts.index(e_host)] += 1
                else:
                    errors_hosts.append(e_host)
                    counts_errors.append(1)

    
    fig_1 = plt.figure()

    fig_2 = plt.figure()

    plt.title('The Error Log')
    plt.xlabel('IPs')
    plt.ylabel('traffic')
    plt.bar(remote_hosts, counts_host, width=0.4)
    plt.savefig('Error_Plot.pdf')

    plt.title('The Error Log(Errors)')
    plt.xlabel('IPs')
    plt.ylabel('traffic')
    plt.bar(errors_hosts, counts_errors, width=0.4)
    plt.savefig('Error_Users_Plot.pdf')
          

plotGraph()

