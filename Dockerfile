FROM voidlinux/voidlinux

RUN xbps-install -Svuy
RUN xbps-install python3-pip bash
RUN whereis pip
RUN whereis pip3
#RUN pip3 install pelican Markdown ghp-import shovel
#RUN pip3 install --upgrade pelican Markdown ghp-import shovel

# Install script to ensures that newly created files are 775 by default
#ADD docker-umask-wrapper.sh /bin/docker-umask-wrapper.sh
#RUN chmod u+x /bin/docker-umask-wrapper.sh

WORKDIR /srv/pelican-website

# Expose default Pelican port
EXPOSE 8000

# Run Pelican
#CMD make devserver
