#!/bin/bash

# Clean previous simulation files
echo "Cleaning previous simulation files..."
rm -rf __pycache__
rm -rf results.xml
rm -rf combined_results.xml
rm -rf log.txt
rm -rf sim_build
rm -rf modelsim.ini
rm -rf transcript
rm -rf vsim.wlf
# Run make to build the simulation
echo "Running Makefile..."
make