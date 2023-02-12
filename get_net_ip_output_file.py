from ip_address_net_id import  Network_IP_Address_ID
import csv

file_db = "file_name.csv"
out_put_f = "out_put_file.csv"

with open(file_db, 'r') as file_csv1:
    csv_reader = csv.reader(file_csv1)
    with open(out_put_f, "w") as file_csv2:
        
        for line in csv_reader:
            ip = Network_IP_Address_ID(line[1],line[2])
            file_csv2.write(f"{line[0]},{ip},{line[1]},{line[2]},{line[3]}\n")
