#!/bin/sh
home_dir=`pwd`
source .env

# Deploying crwd-bsod-discovery-lambda-function 
cd ${home_dir}/lambda/crwd-bsod-discovery-lambda-function/
serverless package
cur_dir=`pwd`
lambda_dir=`basename ${cur_dir}`
aws s3 cp ${cur_dir}/.serverless/*.zip s3://${LAMBDA_S3_BUCKET}/lambda/${lambda_dir}.zip

# Deploying ebs-attach-lambda-function
cd ${home_dir}/lambda/ebs-attach-lambda-function/
serverless package
cur_dir=`pwd`
lambda_dir=`basename ${cur_dir}`
aws s3 cp ${cur_dir}/.serverless/*.zip s3://${LAMBDA_S3_BUCKET}/lambda/${lambda_dir}.zip

# Deploying ebs-detach-lambda-function
cd ${home_dir}/lambda/ebs-detach-lambda-function/
serverless package
cur_dir=`pwd`
lambda_dir=`basename ${cur_dir}`
aws s3 cp ${cur_dir}/.serverless/*.zip s3://${LAMBDA_S3_BUCKET}/lambda/${lambda_dir}.zip