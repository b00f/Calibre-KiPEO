zip_contents = libpyarabicshaping/* images/* *.py LICENSE *.md *.txt

all: compress

compress:
	@ rm -f KiPEO.zip
	@ echo "Create a zip file..." && zip "kipeo.zip" $(zip_contents)