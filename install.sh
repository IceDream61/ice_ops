#!/bin/bash -e

read -p "Install vim config? [Y/n] " order
case $order in
    [nN][oO]|[nN])
        ;;
    *)
        echo "install vim config ..."
        cp -r vim ~/.vim
        cp vimrc ~/.vimrc
        ;;
esac
