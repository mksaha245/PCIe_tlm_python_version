# PCIe
Command line for running the main.py file:
  
$ python3 main.py --num_pkts=20 --err_eij=1 --err_pkt_no=10 --ep_err_eij=1 --ep_err_pkt_no=5 --num_ep_pkt_tx=20 --test=cfg_with_mem_seq_test
  
[By default num_pkts = 100, err_eij = 0, err_pkt_no = 0, ep_err_eij = 0, ep_err_pkt_no = 0]
    
>>num_pkts          ->Declared as int datatype  
                    ->Total no. of packets you need to be generate
    
>>err_eij           ->Declared as bit datatype
                    ->Used for Enabling or Disabling the error injection
    
>>err_pkt_no        ->Declared as bit datatype
                    ->Total no. of error packets need to be injected
                    
>>ep_err_eij        ->Declared as bit datatype
                    ->Used for Enabling or Disabling the error injection from completer
    
>>ep_err_pkt_no     ->Declared as bit datatype
                    ->Total no. of error packets need to be injected from completer
    
>>num_ep_pkt_tx     ->Declared as bit datatype
                    ->Total no. of packets you need to be generate from End-Point                    
    
>>test              ->Declared as string datatype
                    ->By default CFG packets will be sent, and if given 'cfg_with_mem_seq_test' than CFG and MEM both will be sent                
                    
                    
# PCIE Python and Verilog Components Readme

[![Build Status](https://github.com/mukesh891/PCIe_main_repo)]

GitHub repository: https://github.com/mukesh891/PCIe_main_repo

## Introduction

Collection of PCIE TLP related components. Implementation done for Python part,
UVM  is  under  progress. The  whole  project is  based  on Transaction  layer
sendinf packets from RC (Root Complex) to the End Point(EP) with type 0 packets.
packet is being generated from  the  RC  side and is  recieved by EP, basically
2 kinds of packets have been implemented i.e config packets and memory sequence
packets , during  this  process  there  are  other features that included error
injection  from  RC as  well as EP side using uvm_callback class. The number of
packets and enabling error injection from both side are being controlled by the
help of command line arguments Example  designs  implementing a simple UDP echo
server are included for the 

following simulators are used:

*  Questa_10.7d 
	-> questa insatllation(application for windows)
		link -> https://youtu.be/WgyNRYXe2dc
*  Python-3.6
	-> python installation commands
		$wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
		$tar -xf Python-3.7.12.tgz
		$cd Python-3.7.12
		$./configure --enable-optimizations
		$make altinstall
//Arguments used:
//Output files Generated:
//How RC Side Generator Works:
//How EP Side Checker Works:
//ERROR INJECTION ENABLING:


## Documentation

### `pcie_tlp_top.sv` extends form uvm_sequnce_item module
### `pcie_tlp_rc_.sv` extends form uvm_sequnce_item module
### `pcie_tlp_seq_item_pkg.sv` extends form uvm_sequence_item module
Containing all the tlp signals in encapsulated format

### `pcie_tlp_rc_virtual_sequence.sv` extends form uvm_sequence module

### `pcie_tlp_rc_config_sequence.sv` extends form uvm_sequence module

### `pcie_tlp_rc_mem_sequence.sv` extends form uvm_sequence module

### `pcie_tlp_rc_tx_monitor.sv` extends form uvm_monitor module
### `pcie_tlp_rc_rx_monitor.sv` extends form uvm_monitor module
### `pcie_tlp_rc_rx_pkt_checker.sv` module
### `pcie_tlp_rc_virtual_sequencer.sv` extends form uvm_sequencer module
### `pcie_tlp_rc_config_sequencer.sv` extends form uvm_sequencer module
### `pcie_tlp_rc_mem_sequencer.sv` extends form uvm_sequencer module

