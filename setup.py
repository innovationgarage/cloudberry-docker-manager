#!/usr/bin/env python

import setuptools

setuptools.setup(name='cloudberry-docker-manager',
      version='0.1.1',
      description='A docker container manager for Cloudberry',
      author='Egil Moeller',
      author_email='egil@innovationgarage.no',
      url='https://github.com/innovationgarage/cloudberry-docker-manager',
      packages=setuptools.find_packages(),
      install_requires=[
          'cloudberry-netjson',
          'docker',
          'click'
      ],
      entry_points='''
      [console_scripts]
      cloudberry-docker-manager = cloudberry_docker_manager.cli:main
      '''
  )
