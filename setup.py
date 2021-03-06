from setuptools import setup
# Install with:
# 	apt-get install python3-pip
#	pip3 install setuptools
#   if required: apt-get install python3-lxml
#	python3 setup.py install
# To generate executables (post install): 
#   pip3 install pyinstaller
#   Change according to version/OS
#     pyinstaller CoversDownloader.py -F -n ComicbookCoversDownloader1.3.exe --specpath Build --distpath Releases --workpath Build
#	if required: /home/username/.local/bin/pyinstaller aka https://stackoverflow.com/questions/38746462/how-to-correctly-install-pyinstaller 

setup(  name = 'Comicbook Covers Downloader',
        version = '1.3',
        description = 'Webscraper for DC, Marvel and more Comicbook Wikias to download CB covers',
        author = 'F del Mazo',
		author_email = 'federicodelmazo@hotmail.com',
		url = 'https://github.com/FdelMazo/ComicbookCoversDownloader/',
		install_requires = ['lxml', 'bs4', 'requests'],
)
