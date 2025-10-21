#!/bin/bash

aws dynamodb create-table --cli-input-json file://customers-table.json

Start-Sleep -Seconds 60

#! gitbash or linux
#!sleep 60 

aws dynamodb batch-write-item --request-items file://customer-items.json