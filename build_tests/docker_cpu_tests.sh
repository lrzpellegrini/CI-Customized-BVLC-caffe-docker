#!/usr/bin/env bash
set -e
docker run --rm -v "$PWD:/opt/project" "$CPU_IMAGE_TAG" ./execute_tests.sh
echo "CPU tests completed"
