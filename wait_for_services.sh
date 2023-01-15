#!/bin/bash

# Wait for dependencies to start properly
echo "Waiting for services to start..."
wait-for-it -q mysql:3306 || exit $?
wait-for-it -q rabbitmq:5672 || exit $?

# Run the actual command
exec "$@"
