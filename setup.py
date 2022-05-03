import setuptools

setuptools.setup (
  include_package_data = True, 
  name='mycalc0001',
  version='0.0.1',
  description='oss-dev my calculator 0001',
  author='sejinchun',
  author_email='sjchun@dau.ac.kr',
  url = "https://github.com/sejin-chun/calc0001",
  download_url = "https://github.com/sejin-chun/calc0001/archive/refs/tags/v0.0.1.zip",
  install_requires=['pytest'],
  long_description = 'oss-dev calculator python module',
  long_description_content_type = 'text/markdown',
  classifiers=[
      "Programmming Language :: Python :: 3",
      "Operating System :: OS Independent",
  ],
)
  
