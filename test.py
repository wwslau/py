import boto3

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print instance.id, instance.instance_type

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)