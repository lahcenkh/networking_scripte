
# this function is used for output deffirent format of MAC Addresses

def filter_mac(mac_address,spliter_symbole,nb_of_char):
    mac = str(mac_address)
    resulte = []
    
    # remove any sepiale characher
    
    if(mac.__contains__('-')):
        mac_sp = mac.replace('-','')
    elif(mac.__contains__(':')):
        mac_sp = mac.replace(':','')
    elif(mac.__contains__('.')):
        mac_sp = mac.replace('.','')
    
    # create a new list dependent on MAC address format

    for i in range(0, len(mac_sp), nb_of_char):
        resulte.append(mac_sp[i:i+nb_of_char])

    # join MAC Address 
    mac_filtered = f"{spliter_symbole}".join(resulte)
    return mac_filtered.lower()

MacAddress = filter_mac("12-E5-BC-4D-91-99", ".", 4)

print(MacAddress)