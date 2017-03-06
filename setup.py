from setuptools import setup

setup(name='flavors',
      version='0.1',
      description='Flavor Library',
      keywords='flavors wheel tasting',
      url='https://github.com/gtoutoungis1/flavors',
      author='Graziella Toutoungis',
      author_email='graziella.toutoungis@gmail.com',
      license='',
      packages=['flavors'],
      install_requires=[
          'fuzzywuzzy',
          'python-Levenshtein'
      ],
      zip_safe=False)
