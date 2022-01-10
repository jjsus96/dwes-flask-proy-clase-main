FROM python:3.9-bullseye


# Non-root user
RUN useradd -m worker
# Set user
USER worker
# Set the working directory to the root of the project /app
WORKDIR /home/worker
# Copy local contents into the container
COPY --chown=worker:worker requirements.txt requirements.txt
#ADD . /home/worker/
# Install dependencies
RUN pip install -r requirements.txt

ENV PATH='/home/worker/.local/bin:/usr/bin/:$PATH'
COPY  --chown=worker:worker . .
# Listen on port 5000
EXPOSE 5000
# Run the app
ENTRYPOINT [ "python3" ]
CMD [ "main.py"]