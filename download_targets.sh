#!/usr/bin/env bash

bins=(basic1 basic2 basic3 intermediate1 intermediate2 intermediate3 advanced1 advanced2 advanced3)

rm -f targets/*

for b in "${bins[@]}"
do
    curl -o targets/$b "https://github.coventry.ac.uk/pages/csx239/naturan_demanto/bins/$b"
done

chmod u+x targets/*
