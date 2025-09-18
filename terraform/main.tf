provider "aws" {
  region = var.aws_region
}

# Security group to allow port 8000
resource "aws_security_group" "mlops_sg" {
  name        = "mlops-sg"
  description = "Allow HTTP traffic on port 8000"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 instance
resource "aws_instance" "mlops-capstone_ec2" {
  ami           = var.ami
  instance_type = var.instance_type
  security_groups = [aws_security_group.mlops_sg.name]
  key_name      = var.key_name
  user_data     = file("user_data.sh")

  tags = {
    Name = "FastAPI-Server"
  }
}
