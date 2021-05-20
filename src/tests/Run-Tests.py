import os

os.system("pytest -v -s --driver=chrome --alluredir="'C:\AllureReports\Data'"")


# Run Docker server
# docker run --rm -ti --name zalenium -p 4444:4444 -p 5555:5555 -v /var/run/docker.sock:/var/run/docker.sock dosel/zalenium start