#!/usr/bin/python

import subprocess

print('----------------------------------------------------')
print('----------Starting MYSQL Local Database ------------')
print('')
print('Going into docker_db directory...')
print('Killing running ipt_local_db container..')
subprocess.call('docker kill ipt_local_db',shell=True)
print('run docker-compose up --build')
subprocess.call('docker-compose up --build &',shell=True)
print('Docker container is running in the background')

