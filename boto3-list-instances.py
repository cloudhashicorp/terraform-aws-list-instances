import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    # filter the instances based on filters() above
    instances = ec2.instances.all()

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print (instance.id, instance.private_ip_address, instance.state)
