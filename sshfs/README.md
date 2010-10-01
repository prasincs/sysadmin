About
====

This is supposed to make mounting and unmounting ssh partitions easier in OS X. 

You'll need:

 - [MacFUSE](http://code.google.com/p/macfuse/)

 - SSHFS binary (I have included the binary for Leopard/Snow Leopard here)

put these two files (sshfs and sshfsmount) in your path and grant executable permissions. I generally put them in the $HOME/bin directory and put 
	$PATH=$HOME/bin 
in my ~/.bash_profile file. Alternatively you can put it in your /usr/bin or /opt/local/bin folder

You'll need to create a conf file in ~/.sshmount.conf with the following format (as shown in the sample)

	#name	server	username	remotedir	localdir	volname
	name	server.com	username	/home/username	/tmp/mnt	MyVolume

replace the content in the second line with your server name, where you want to mount it and stuff.


Usage
=====
To mount, do

	sshmount <name>

To unmount, do

 	sshmount -u <name>
