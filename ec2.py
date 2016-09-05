import boto3

s = boto3.resource('ec2')
for i in s.instances.all():
    print(i)