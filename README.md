# Website_Surveillance-Script
A script that checks my personal site for proper responses, if it detects an issue it wil send a email alert and Reboot Servers.

So, since I am experimenting with my server in different fire wall mechinisms and site deployments like Apache2, Eginx, Etc., 
and I also only pay for the most minimal CPU requirements that I can get by with, its nice to know if my server has crashed 
and have a mechinism in place to restart my server, so I wrote this script in Python to scan my site for the
proper http responses and If it dectects any thing other then a 200 or exception response it will notify me by email with the smptlib 
and trigger a restart of my linode server using A Linode Api I set up useing a token. I set all my Keys with path varibles direct from my 
operating system, though their are more secure path input methods I could of used. I have the script currently running on my windows os every 15 min with the task scheduler, though I plan on running it from the $crontab in my linux/Ubuntu os.
