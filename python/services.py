#!/usr/bin/env python

# Created to read all the XML files created by nagios and strip the variables of interest
# with the intention of eventually graphing it in Grafana.

import untangle
import os

directory = '/opt/omd/sites/org/var/pnp4nagios/perfdata/'
host_dict = {}
service_dict = {}
wanted_hosts = ( "APP*", )
wanted_services = ( "MySQL_Threads_connected",
                    "Memory_used", 
                    "web-response-time",
                  )

def compile_hostservices():
  for host in os.listdir(directory):
    host_dict[host]={}
    for file_name in os.listdir( directory + host ):
      if file_name.endswith(".xml"):
          service = os.path.splitext(file_name)[0]
          #print "host=%s service=%s file_name=%s" % ( host,service,file_name)
          host_dict[host][service]=file_name


def list_hostservices():
  for host in host_dict.keys():
    for service in host_dict[host]:
      print ("Host: %s, Service: %s" % ( host, service))


def getinfo (host, service):
    if "*" in host:
      host = host.rstrip('*')
      for key in host_dict.keys():
        if key.startswith(host):
            if service in host_dict[key].keys():
              obj = untangle.parse(directory+key+'/'+host_dict[key][service])
              print key, " -> " , service , ":"
              for item in obj.NAGIOS.DATASOURCE:
                print "Name: ", item.NAME.cdata
                print "Act:  ", item.ACT.cdata
                print "Max: ", item.MAX.cdata
  

if __name__ == '__main__':
  # Compile all avaliable hosts and their services
  compile_hostservices()
  for host in wanted_hosts:
    for service in wanted_services:
      getinfo(host,service)

