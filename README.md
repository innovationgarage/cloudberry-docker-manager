# cloudberry-docker-manager

This program is intended to be used in conjunction with https://github.com/innovationgarage/cloudberry-lede-openwisp-docker
and https://github.com/innovationgarage/cloudberry-netjson to configure docker using OpenWISP to run a set of containers with openWRT, each also configured using OpenWISP.

Usage:

    cloudberry-docker-manager init BASE_URL UUID KEY
    while sleep 5; do cloudberry-docker-manager update; done

In production, a cronjob should be set up to run 'update'.

The manager assumes that there is a docker image tagged *cloudberry-lede-openwisp-docker:latest* already available (unless the openwisp supplied config says to use another image). This image can be constructed by building https://github.com/innovationgarage/cloudberry-lede-openwisp-docker
