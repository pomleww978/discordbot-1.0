import C_F
import json
import sys

C_F.log()
def on_start_IFN() :

    with open ('status/IFN.json') as json_IFN_file :
        data = json.load(json_IFN_file)
    
    if data["on_start_active"] == "yes" :
        C_F.log_logger('debug', f'start IFN security system {data["version"]} ')
        print("active key correct IFN has start")
        
    elif data["on_start_active"] == "no" :
        
        ACK = str(input("IFN active key > "))

        if data['active_key'] == ACK :
            C_F.log_logger('debug', f'start IFN security system {data["version"]} ')
            print("active key correct IFN has start")
            ACP = str(input('want to open a on_start_active (y,n) > '))

            if ACP == 'y' :
                data['on_start_active'] = 'yes'
                with open ('status/IFN.json', 'w') as IFN_onstart :
                    json.dump(data , IFN_onstart)

        else :
            print("password incorrect active IFN fail")
            C_F.log_logger('debug', 'IFN start fail active key incorrect')

on_start_IFN()