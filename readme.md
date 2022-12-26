# Auto run nginx container python script

**This code is only to explore the docker lib**

**it's not done for production**

### You will need

1. docker
2. nginx image on docker
    ```shell
    docker pull nginx:latest
    ```
3. python3

### How to run

1. install requirements
    ```shell
    pip3 install -r ./requirements.txt
    ```
2. you should have docker up
    ```shell
    sudo service docker start
    ```
    ```shell
    sudo systemctl start docker.service
    sudo systemctl start docker.socket
    ```
3. run the script
    ```shell
    ./main.py
    ```

if you open process list

```shell
ps -eaf --forest
```

you will see something like that

```
root       20578       1  0 20:07 ?        00:00:00 /usr/bin/containerd-shim-runc-v2 -namespace
root       20600   20578  0 20:07 ?        00:00:00  \_ nginx: master process nginx -g daemon of
systemd+   20652   20600  0 20:07 ?        00:00:00      \_ nginx: worker process
systemd+   20653   20600  0 20:07 ?        00:00:00      \_ nginx: worker process
systemd+   20654   20600  0 20:07 ?        00:00:00      \_ nginx: worker process
systemd+   20655   20600  0 20:07 ?        00:00:00      \_ nginx: worker process
```

if you kill the parent process, in this case pid `20578` the program will remove the exited container and will start another one
