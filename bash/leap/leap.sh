#!/usr/bin/env bash

main () {
    local year=$1;
    if [ $($year % 4) ==  0 ] \
           && ! [ $($year % 100) == 0 ] \
           && ! [ $($year % 400) == 0 ] ; then
        echo "True"
    else
        echo "False"
    fi
}

main "$@"