Enable Autologin in Ubuntu Server from Commandline
If you're using Ubuntu Server, typically it doesn't come with a graphical user interface (GUI) by default and uses a command-line interface. Therefore, the concept of auto-login for a GUI-based desktop environment doesn't apply here.

However, if you want to set up automatic login to the command-line console (TTY) that you see after booting your server, you can follow these steps:

1. First, open the /etc/systemd/logind.conf file in a text editor as sudo or root user. Here we'll use nano:

$ sudo nano /etc/systemd/logind.conf
2. In the opened file, look for a line that starts with #NAutoVTs=. Uncomment it by removing the # at the beginning of this line. After the = sign, enter the number of TTYs you want to be logged in automatically. For example, NAutoVTs=6 would auto-login the first 6 TTYs.

3. Next, look for a line that starts with #ReserveVT= and uncomment it by removing the #. After the = sign, put the number of the first TTY that you want to skip auto-login for. So, if you want to auto-login TTYs 1-6, you would put ReserveVT=7 to start reserving from the 7th TTY.

Set the Number of TTYs
Set the Number of TTYs
The two directives "NAutoVTs" and "ReserveVT" are configurations related to the systemd-logind service, which handles user logins in a Linux system and are typically found in the logind.conf file.

NAutoVTs: This directive sets the number of virtual terminals (VTs) to allocate by default that systemd-logind will manage. This does not mean that no more than this number of VTs can exist, just that systemd-logind will not automatically allocate more than this. The virtual terminals are allocated on-the-fly as they are needed.
ReserveVT: This directive sets the number of the first virtual terminal that shall unconditionally be reserved for a getty. This means that no graphical login (like a desktop manager) can allocate this terminal. If this is set to 0, no terminal is unconditionally reserved.
Essentially, these directives control how many virtual terminals are allocated and managed by systemd-logind and which ones are reserved for certain types of usage.

4. Press CTRL+O followed by CTRL+X to save the file and exit the text editor.

5. Now, you need to create a service to auto-login your user. To do so, create a directory named "getty@tty1.service.d" under /etc/systemd/system/ location.

$ sudo mkdir /etc/systemd/system/getty@tty1.service.d/
Replace tty1 with tty2, tty3, etc., in the command above for each TTY that you want to auto-login.

Use the following command to create a service for the first TTY:

$ sudo nano /etc/systemd/system/getty@tty1.service.d/override.conf
6. In the opened file, paste the following lines:

[Service]
ExecStart=
ExecStart=-/sbin/agetty --noissue --autologin ostechnix %I $TERM
Type=idle
Configure Autologin in Ubuntu Server
Configure Autologin in Ubuntu Server
Replace ostechnix with your actual username. Save the file and exit.

Let us break down the above code and see what each option does.

[Service]: This is a section that specifies the behavior of the service itself. The directives inside this section will control how the service starts and stops, its timeout values, and more.
ExecStart=: This directive specifies the command to run when the service starts. The equal sign followed immediately by nothing is a way to reset the list of commands to run, in case it was set in another file that this service file is overriding.
ExecStart=-/sbin/agetty --noissue --autologin ostechnix %I $TERM: The new command to run when the service starts. Here, /sbin/agetty is being called with several parameters. agetty opens a tty port, prompts for a login name, and invokes the /bin/login program. The --noissue parameter prevents display of the /etc/issue file before the login prompt. --autologin ostechnix logs in the user ostechnix automatically. %I is a specifier that systemd replaces with the instance name (the tty in this case). $TERM is an environment variable defining the type of the terminal.
Type=idle: This directive tells systemd to wait until all jobs are dispatched before it starts the service. This ensures that the service won't start until the system is idle, freeing up resources.
7. Repeat steps 5-7 for each TTY that you want to auto-login.

8. Finally, reboot your server to apply the changes:

$ sudo reboot
