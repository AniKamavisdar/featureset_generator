#MOCKING SYS ARGUMENT PASS
from os import environ as env


print("RUNNING TEST SCRIPT")
env['ENV'] = 'dev'
env['FEATURE_OUTPUT_LOC']='/Users/aniketkamavisdar/IpyNotebooks/featureSet_export/'
env['test_']=env['PWD']+'/..'+'/test_confs'
env['GOOGLE_APPLICATION_CREDENTIALS'] = env['test_']+"/prod-bigquery.json"

from src import main

main.__main()
