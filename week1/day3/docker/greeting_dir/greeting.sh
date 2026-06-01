#!/bin/bash
greeting_word=$1
while IFS= read -r line; do
    echo $greeting_word "$line"
done < "clean_names.txt"
