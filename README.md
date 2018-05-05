# cloudberry-docker-manager

This program is intended to be used in conjunction with [innovationgarage/cloudberry-lede-openwisp-docker][0] and
[innovationgarage/cloudberry-netjson][1] to configure docker using [OpenWISP][2] to run a set of containers with
[OpenWrt][3], each also configured using OpenWISP.

Usage:

    cloudberry-docker-manager init BASE_URL UUID KEY
    while sleep 5; do cloudberry-docker-manager update; done

In production, a cronjob should be set up to run 'update'.

The manager assumes that there is a docker image tagged
*cloudberry-lede-openwisp-docker:latest* already available (unless the OpenWISP
supplied config says to use another image). This image can be constructed by
building [innovationgarage/cloudberry-lede-openwisp-docker][4].

## See also

* [djangoproject](https://github.com/innovationgarage/cloudberry-djangoproject) - Centralized configuration web UI
* [lede-openwisp-docker](https://github.com/innovationgarage/cloudberry-lede-openwisp-docker) - OpenWISP docker image

[0]: https://github.com/innovationgarage/cloudberry-lede-openwisp-docker
[1]: https://github.com/innovationgarage/cloudberry-netjson
[2]: http://openwisp.org/
[3]: https://openwrt.org/
[4]: https://github.com/innovationgarage/cloudberry-lede-openwisp-docker
