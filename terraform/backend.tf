terraform {
  backend "s3" {
    # These values will be set by deployment scripts
    # For local development, they can be passed via -backend-config
  }
}



#terraform apply -target=aws_s3_bucket.terraform_state -target=aws_s3_bucket_versioning.terraform_state -target=aws_s3_bucket_server_side_encryption_configuration.terraform_state -target=aws_s3_bucket_public_access_block.terraform_state -target=aws_dynamodb_table.terraform_locks