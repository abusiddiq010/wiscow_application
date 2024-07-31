# Use an official lightweight base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*
ENV PATH="/usr/games:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
# Copy the script into the container
COPY wiscow.sh /usr/local/bin/wiscow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wiscow.sh

# Expose the port the server will run on
EXPOSE 4499

# Run the script
CMD ["/usr/local/bin/wiscow.sh"]
