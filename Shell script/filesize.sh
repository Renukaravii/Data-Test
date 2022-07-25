#!/bin/sh
#sh filesize.sh renault-dgc-epi-6220-archive-ope/customer_forecast_order_nna 2022-06 2022-07
echo "project name and table is :"$1
echo "current month is:"$2
echo "previous month is:"$3
gsutil ls -l -h gs://$1|grep -i $2> input.txt
gsutil ls -l -h gs://$1|grep -i $3>> input.txt
input='input.txt'
while read -r line; 
do 
awk '$1=$1';
done < "$input" > output4.txt
input='output4.txt'
while read -r line; 
do
tr -s ' ' ',';
done < "$input" > output5.csv
awk -F, '{$5=substr($3,0,10);}1' OFS=, output5.csv > date.csv
awk -F, '{$6=substr($3,12,3);}1' OFS=, date.csv > time.csv
awk -F, '{$7=substr($4,87,20);}1' OFS=, time.csv > final.csv
{ echo "file_size,file_type,date and time,path,date,time,pattern"; cat final.csv;} >epi.csv
rm date.csv time.csv output4.txt output5.csv final.csv input.txt




