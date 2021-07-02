#!/bin/bash

echo "dev logs check"
ls -l ./logs/dev/*

echo "remove dev logs"
rm ./logs/dev/*

echo "dev logs check"
ls -l ./logs/dev/*
