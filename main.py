#!/usr/bin/env python3

from time import sleep
import docker

print("RUNNING");

docker_client = docker.from_env()

def list_containers():
    containers = docker_client.containers.list(all=True)

    return containers

def start_nginx_container():
    ports = {
        '80/tcp': ('127.0.0.1', 8080)
    }

    container = docker_client.containers.run('nginx:latest', detach=True, ports=ports)
    container.logs()

    return container

def quit(noprint=False):
    print()

    if not noprint:
        print()
        print("stopping containers")

    containers = list_containers()

    for container in containers:
        if not noprint:
            print(f"[{container.status}] stopping {container.id}")
        container.stop()
        container.remove()

quit(True)
start_nginx_container()

while True:
    try:
        sleep(1)

        containers = list_containers()
        print(f"{len(containers)} running")

        if containers[0].status != 'running':
            quit(True)
            print("deploying one container")
            container = start_nginx_container()
            print(f"container {container.id} is [{container.status}]")
    except:
        quit()
        break

