#!/bin/bash

if (($# != 1))
then 
    echo "Please provide the current year to generate the base files."
else 
    mkdir -p "$1"

    for var in {1..25}
    do 
        mkdir -p "$1/Day $var"/{"Challenge 1","Challenge 2"}
    done
fi