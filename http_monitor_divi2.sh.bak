#!/bin/bash
wget --http-user=nms --http-passwd=970811 http://saier.ivi2.org:8036/cgi-bin/nph-xlat-list?00:1e:67:e6:62:4b+20
sed '1,9d' nph-xlat-list\?00\:1e\:67\:e6\:62\:4b+20 > for_nph.txt
var=`cat for_nph.txt | awk '{print $8}'`
b=($(tr "|" " " <<< $var))
echo ${b[1]}
if [ `echo "${b[1]%?} > 10" | bc` -eq 0 ]
then
  echo "error" | mail -s "low flow" 1852591770@qq.com 
else 
  echo 2
fi
rm nph-xlat-list?00:1e:67:e6:62:4b+20
