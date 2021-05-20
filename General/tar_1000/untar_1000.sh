#!/bin/bash

i=1000
until [ $i -lt 1 ]
do
    tar -xvf $i.tar.gz
    rm -rf $i.tar.gz
    ((i--))
done

echo "All done"
