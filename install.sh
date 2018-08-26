#!/bin/bash

$PWD/helpers/nvm.sh

echo $(node --version)
echo $(npm --version)

cd /ubuntu
npm i

node ubuntu.js
