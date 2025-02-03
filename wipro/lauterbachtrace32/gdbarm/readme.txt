Dear User,

this demo shows how to use the TRACE32 GDB FrontEnd for ARM.

The demo supposes that an ARM GDB server is already running.

First you have to configure the remote connection parameters.

The default setting (PBI=GDB COM1 baud=115200) in the enclosed file config.t32 
supposes that a connection via a serial port is used.

Alternatively you can configure a TCP connection by replacing (PBI=GDB COM1 baud=115200) by one of the following lines:

PBI=GDB  <remote_target_ip_address>:<gdb_port>
e.g. PBI=GDB  127.0.0.1:30000

or

PBI=GDB  <host_name>:<gdb_port>
e.g. PBI=GDB  localhost:30000


Now you can start t32marm.exe. The next step is to inform TRACE32 about
the CPU you are using on your target. The default CPU is arm720t.

Enter the command 
SYStem.CPU 
to the TRACE32 command line and select your target CPU in the SYStem.CPU dialog.

Finally you have to establish the connection between the ARM GDB server
and TRACE32, by entering the command:
SYStem.mode Attach

Now you can start to debug.

For more details about the TRACE32 GDB FrontEnd please refer to
http://www.lauterbach.com/pdf/frontend_gdb.pdf


RTOS and Case Tool support files are not included in the demo package.

The HELP command (or menu) provides access to the online manuals.
The manual is reduced version of the full online manual.
The "Simulator Tutorial" chapter helps to make the first steps.

For updates and new versions of this debugger please check in 

http://www.lauterbach.com.


Best Regards

The Lauterbach Team
