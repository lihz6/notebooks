#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

jupyter notebook --no-browser --notebook-dir="$BASEDIR"
