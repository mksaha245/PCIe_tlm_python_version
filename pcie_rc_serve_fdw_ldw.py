from pcie_lib import *

#req.header_mem.last_dw inside {0,1,3,7,15};
#req.header_mem.first_dw inside {0,8,12,14,15};

#def pcie_rc_serve_fdw_ldw(payload,fdw,ldw):
def pcie_rc_serve_fdw_ldw():
    #first_dw_be = fdw
    first_dw_be = '1000'
    last_dw_be = '0011'
    payload = '00101111001010110000011101100101';
    print(hex(int(payload,2)))
    data = payload[len(payload)-32:]
    f_data = int(data,2)
    byte1 = f_data  & 0xFF
    byte2 = f_data  & 0x0000FF00
    byte3 = f_data  & 0x00FF0000
    byte4 = f_data  & 0xFF000000
    ################################
    ## Note : Getting payload according to first_dw_be 
    if first_dw_be == "0000": 
        f_data = format(0,'032b')
    elif first_dw_be == "1111":
        f_data = byte4 + byte3 +byte2 +byte1 
    elif first_dw_be == "1110":
        f_data = byte4 + byte3 +byte2  
    elif first_dw_be == "1100":
        f_data = byte4 + byte3
    elif first_dw_be == "1000":
        f_data = byte4

    fdw_data = '0X'+'{:08X}'.format(f_data)
    print(fdw_data)
    ################################
    if last_dw_be == "0000": 
        l_data = format(0,'032b')
    elif last_dw_be == "0001":
        l_data = byte1 
    elif last_dw_be == "0011":
        l_data = byte1 + byte2 
    elif last_dw_be == "0111":
        l_data = byte1 + byte2 + byte3 
    elif last_dw_be == "1111":
        l_data = byte1 + byte2 + byte3 + byte4 
    '''
    if int(first_dw_be,2) >0 :
        offset = offset+'00'
    elif int(first_dw_be,2) >=2 :
        offset = offset+'01'
    elif int(first_dw_be,2) >=4 :
        offset = offset+'10'
    elif int(first_dw_be,2) ==8 :
        offset = offset+'11'
    '''
    ldw_data = '0X'+'{:08X}'.format(l_data)
    print(ldw_data)

pcie_rc_serve_fdw_ldw()



