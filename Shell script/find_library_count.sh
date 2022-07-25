#!/bin/ksh
#sh find_library_count.sh com.renault.pan.data.model.mpd.DataRecordModel pan-ingestion-trm----correct library
#sh find_library_count.sh qqq pan-ingestion-trm----wrong library
echo "project file" $2
mkdir pan-ingestion-trm_project
unzip $2 -d pan-ingestion-trm_project
cd pan-ingestion-trm_project
echo "library name:" $1
grep -r $1
if [ $? == 0 ] ; then
echo "The given library is present in the project file"
echo " The count of the library is"
grep -r $1 | wc -l
else
echo "no such library found....please enter correct library name"
fi