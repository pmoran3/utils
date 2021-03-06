#!/bin/csh -f

# Crontab command for every 4 hours at the 44 minute
# 44 */4 * * * ~/volatileQuery.sh 

set dataDir   = /group/clas/www/gemc/html/web_interface/data
set scriptDir = /group/clas12/SubMit/utils/

if($1 == 'test') then
	echo running test
	set dataDir   = /group/clas/www/gemc/html/test/web_interface/data
	set scriptDir = /group/clas12/SubMit/test/SubMit/utils/
endif

### going to web interface data
rm $dataDir/volatile.log
cd /volatile/clas12/osg
nice +20 du -B G -d 2 -t 1 | grep -v lund | grep -v gemc | grep -v test > $dataDir/volatile.log
cd $dataDir
python $scriptDir/jsonify_disk_usage.py --logfile volatile.log --output disk.json
