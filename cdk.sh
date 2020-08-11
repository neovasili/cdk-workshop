#!/usr/bin/env bash

if [[ $# -ge 1 ]]; then
  if [[ $# -ge 2 ]]; then
    stage="$2"
  else
    stage="dev"
  fi
  export STAGE="$stage"
  cdk "$1"
else
  echo "You have to provide at least the command argument"
fi