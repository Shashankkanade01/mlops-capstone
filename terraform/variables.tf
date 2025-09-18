variable "aws_region" {
  default = "ap-south-1"  # Change if needed
}

variable "instance_type" {
  default = "t3.micro"
}

variable "ami" {
  # Ubuntu 22.04 LTS in ap-south-1
  default = "ami-0861f4e788f5069dd"
}
    
variable "key_name" {
  description = "AWS key pair for SSH access"
  default     = "mlops-assignment"  # Replace with your AWS key pair
}

variable "docker_image" {
  description = "Docker image of your FastAPI app"
  default     = "shashankk01/mlops-capstone:latest"  # Replace with your image
}
