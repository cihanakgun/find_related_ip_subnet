import ipaddress

subnets = [('10.129.199.0', '24'), ('10.129.0.0', '16'), ('10.128.0.0', '16')] #subnet,mask
ip_list = ['10.129.199.1','10.129.150.1'] # ip list


def list2ipnetwork(subnets):
    subnet_list = [] # [[IPv4Network('10.129.199.0/24')], [IPv4Network('10.129.0.0/16')], [IPv4Network('10.128.0.0/16')]]
    for subnet in subnets:
        local_subnet_list=[]
        local_subnet_list.append(ipaddress.IPv4Network(str((subnet[0]))+'/'+(subnet[1])))
        subnet_list.append(local_subnet_list)
    return subnet_list

def find_subnet(ip,list):
    belonged_subnets_w_id = []
    belonged_subnets = []
    for prefix in list:
        # print(prefix)
        mini_list = []
        if ipaddress.ip_address(ip) in ipaddress.ip_network(prefix[0]):
            mini_list.append(prefix[0])
            belonged_subnets.append(prefix[0])
            belonged_subnets_w_id.append(mini_list)
    sort_subnet = sorted([ipaddress.ip_network(addr) for addr in belonged_subnets])
    last_subnet=(sort_subnet[-1])
    return last_subnet

parsed_subnets = list2ipnetwork(subnets)
for x in ip_list:
    print(find_subnet(ip=x,list=parsed_subnets))
