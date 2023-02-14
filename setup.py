try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
from os import path
import io

PYPI_VERSION = '0.2.1'

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = find_packages('src')
package_dir = {'': 'src'}

if __name__ == "__main__":
    setup(name='geodata-harvester',
          url="https://github.com/Sydney-Informatics-Hub/geodata-harvester",
          version=PYPI_VERSION,
          description="An automation tool for harvesting and processing geodata from the web",
          long_description=long_description,
          long_description_content_type='text/markdown',
          license='LGPL-3.0',
          install_requires=['numpy',
                            'rasterio',
                            'termcolor',
                            'xarray',
                            'matplotlib',
                            'alive_progress>=3.0.1',
                            'owslib==0.27.2',
                            'netCDF4',
                            'rioxarray',
                            'pyyaml',
                            'pandas',
                            'geopandas',
                            'pyproj',
                            'numba',
                            'shapely',
                            'fiona>=1.8.21',
                            'ipywidgets>=7.6.5',
                            'ipython',
                            'eeharvest',
                            'schema',
                            'requests==2.28.1'
                            ],
          python_requires='>=3.8',
          packages=packages,
          package_dir={'': 'src'},
          include_package_data=True,
          classifiers=['Programming Language :: Python :: 3',
                       'Operating System :: OS Independent',
                       ]
          )
