variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "key_name" {
  type = string
  description = "Existing EC2 Key Pair name"
}

variable "bucket_name" {
  type = string
  description = "Unique name for S3 static website bucket"
}

variable "lambda_zip_path" {
  type = string
  description = "Path to the ZIP file containing your Lambda function code"
}

variable "lambda_function_name" {
  type    = string
  default = "log_s3_events"
}
