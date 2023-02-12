from ip_address_net_id import  Network_IP_Address_ID
import csv

file_db = "MSAN_HW_DB.csv"
out_put_f = "msan_db_net.csv"

with open(file_db, 'r') as nk_ipran_msan:
    csv_reader = csv.reader(nk_ipran_msan)
    with open(out_put_f, "w") as msan_nk_net:
        
        for line in csv_reader:
            ip = Network_IP_Address_ID(line[1],line[2])
            msan_nk_net.write(f"{line[0]},{ip},{line[1]},{line[2]},{line[3]}\n")
