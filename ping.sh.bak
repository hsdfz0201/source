#!/bin/sh
echo "---------------------------------------"
prefixt="SERVER 202.38.101.20 PING $1"
ping6 -w 1 -c 1 $1>/dev/null
ret=$?
if [ $ret -eq 0 ]

then printf "$prefixt OK\n"
else printf "$prefixt ERROR\n" 
     echo "$1" | mail -s "divi2 connect error" 1852591770@qq.com

fi
