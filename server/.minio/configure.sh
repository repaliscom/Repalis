#!/bin/bash

$CMD_MC alias set repalis http://$MINIO_HOST:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD;

# Setup user & acccess policy
$CMD_MC admin user add repalis $ACCESS_KEY $SECRET_ACCESS_KEY
$CMD_MC admin policy create repalis repalis-development $POLICY_FILE
$CMD_MC admin policy attach repalis repalis-development --user $ACCESS_KEY

# Create buckets
$CMD_MC mb repalis/$BUCKET_NAME --with-versioning --ignore-existing

$CMD_MC mb repalis/$PUBLIC_BUCKET_NAME --with-versioning --ignore-existing
$CMD_MC anonymous set download repalis/$PUBLIC_BUCKET_NAME
