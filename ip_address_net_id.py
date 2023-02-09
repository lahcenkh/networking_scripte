def Network_IP_Address_ID(ip,mask):

    #---- splite ip & mask into list -------
    list_IP_Address = ip.split(".")
    list_Mask = mask.split(".")
    #---------------------------------------

    #----- convert ip and mask to binary -----
    def conver_ip_bin(bin_ip,bin_mask):
        Bin_list_IP_Address = []
        Bin_list_Mask = []

        for i, b in zip(bin_ip,bin_mask):
                Bin_list_IP_Address.append(f'{int(i):08b}')
                Bin_list_Mask.append(f'{int(b):08b}')
        return Bin_list_IP_Address , Bin_list_Mask  
    #---------------------------------------------

    #----- get Net ID of IP ---------

    def net_id(ip_nb,mask_nb):
        net_ip_id = []
        for i, j in zip(ip_nb,mask_nb):
            net_ip_id.append(str(int(i) * int(j)))
            
        return "".join(net_ip_id)
    #------------------------------------

    #-------------- get net id of ip address-----------
    bin_ip = conver_ip_bin(list_IP_Address, list_Mask)[0]
    bin_mask = conver_ip_bin(list_IP_Address, list_Mask)[1]

    resulte = []
    for i, b in zip(bin_ip,bin_mask):
        resulte.append(net_id(i, b))
    #--------------------------------------------------

    # ----- convert baniry to decimal ----
    ip_conv_bin_dc = []
    for i in resulte:
        ip_conv_bin_dc.append(str(int(i,2)))

    Net_IP = ".".join(ip_conv_bin_dc)
    return Net_IP

#----------------- for test chose any ip and mask -------------
# print(Network_IP_Address_ID('172.29.14.13', "255.255.255.240"))
