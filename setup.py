'''
Setup tools config for installing PAL client.
'''

from setuptools import setup, find_packages

setup(name='pal_client',
      version='0.0.0',
      packages=find_packages(),
      install_requires=[
          'requests'
      ],
      entry_points={
          'console_scripts': [
              'pal_client = pal_client.__main__:main'
          ]
      },
)
