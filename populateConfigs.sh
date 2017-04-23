#!/bin/bash

echo "Populating configs..";
cp ./.vimrc ~/;
cp ./.lemonsquanch.include ~/;
if [ ! -f "${HOME}/.vimrc_local" ]; then
    cp ./.vimrc_local ~/;
fi

echo "Done!";
