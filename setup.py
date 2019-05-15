from setuptools import setup

setup(name='sms-api-python-demo',
      version='1.0.0',
      description='Learn how to use RingCentral SMS API.',
      license='MIT',
      packages=['sms-api-python-demo'],
      install_requires=[
          'ringcentral',
          'python-dotenv'
      ],
      zip_safe=False)
