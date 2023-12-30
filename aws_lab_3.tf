# provider.tf

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.15.0"
    }
  }
}

provider "aws" {
  region                      = var.region
  skip_credentials_validation = true
  skip_requesting_account_id  = true

endpoints {
    ec2            = "http://aws:4566"
    apigateway     = "http://aws:4566"
    cloudformation = "http://aws:4566"
    cloudwatch     = "http://aws:4566"
    dynamodb       = "http://aws:4566"
    es             = "http://aws:4566"
    firehose       = "http://aws:4566"
    iam            = "http://aws:4566"
    kinesis        = "http://aws:4566"
    lambda         = "http://aws:4566"
    route53        = "http://aws:4566"
    redshift       = "http://aws:4566"
    s3             = "http://aws:4566"
    secretsmanager = "http://aws:4566"
    ses            = "http://aws:4566"
    sns            = "http://aws:4566"
    sqs            = "http://aws:4566"
    ssm            = "http://aws:4566"
    stepfunctions  = "http://aws:4566"
    sts            = "http://aws:4566"
  }
}

variable "ami" {
	type = string
	default = "ami-06178cf087598769c"
}
variable "region" {
	type = string
	default = "eu-west-2"
}
variable "instance_type" {
	type = string
	default = "m5.large"
}

# ssh-key-citadel.tf
resource "aws_key_pair" "citadel-key" {
  key_name   = "citadel"
	public_key = file('/root/terraform-challenges/project-citadel/.ssh/ec2-connect-key.pub')
}

# citadel.tf
resource "aws_instance" "citadel" {
  ami                     = var.ami
  instance_type           = var.instance_type
	user_data = file("/root/terraform-challenges/project-citadel/install-nginx.sh")
	key_name = aws_key_pair.citadel-key.key_name
}

resource "aws_eip" "eip" {
	vpc = true
	instance = aws_instance.citadel.id
	provisioner "local-exec" {
		command = "echo ${self.public_dns} >> /root/citadel_public_dns.txt"
	}
}