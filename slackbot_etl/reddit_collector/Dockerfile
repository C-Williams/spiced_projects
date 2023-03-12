# Specify which version of Python to install on this container
FROM python:3.9

# Where to find necessary files for this container
WORKDIR /app

# Say what files to store and where in the container
COPY . /app

# Tell Docker run these processes at runtime
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Give any necessary commands, language, and file
CMD [ "python","get_reddit.py" ]