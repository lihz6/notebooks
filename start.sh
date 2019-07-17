#!/usr/bin/env bash

BASEDIR=$(dirname $(realpath "$0"))

jupyter notebook --no-browser --notebook-dir="$BASEDIR"
