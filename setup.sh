#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
export TERM=dumb
apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libfreetype-dev libxml2-dev libxslt1-dev
pip install markdown fpdf2
