#!/bin/bash

MAJOR=major
MINOR=minor
MICRO=micro

function usage() {
  echo "Usage: $0 [-a] [-b] [-r [${MAJOR}|${MINOR}|${MICRO}]]"
  echo
  echo "This script is an example"
  echo "    -a : "
  echo "    -b : "
  echo "    -r : "

  exit 0
}

function log() {
  echo -e "$(date -u '+%Y-%m-%dT%H:%M:%S.%NZ')\t$"
}

function printOutput() {
  echo "    ${@}"
}

function banner() {
  message="$1"
  border="$(echo ${message} | sed -e 's+.+=+g')"
  echo "${border}"
  echo "${message}"
  echo "${border}"
}

