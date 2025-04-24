import yaml

raw_yaml = open('Logical_Model.yml', 'r')

Logical_Dict = yaml.safe_load(raw_yaml)

for tenant in Logical_Dict['tenants']:
    print(f"Creating tenant: {tenant['name']}")
    for vrf in tenant['vrfs']:
        print(f"Creating VRF {vrf['name']} for tenant {tenant['name']}")
        for bd in vrf['bds']:
            print(f"Creating bridge domain {bd['name']} for VRF {vrf['name']} for tenant {tenant['name']}")
