#!/bin/bash

if ! type "curl" > /dev/null;
then
  curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

elif ! type "wget" > /dev/null;
then
  wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
else
  sudo apt install wget;
  wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
fi

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

nvm install 8.11
