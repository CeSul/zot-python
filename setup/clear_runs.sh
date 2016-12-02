#!/bin/bash
outputdir='/staging/ess/csul/image_benchmark/output'
cd $outputdir

rm  -r ./output_nodb
mkdir output_nodb

rm -r ./output_read_db
mkdir output_read_db

rm -r ./output_read_write_db
mkdir output_read_write_db
