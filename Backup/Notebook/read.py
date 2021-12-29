import json
import json
from datetime import datetime
filename = datetime.today().strftime('%Y-%m')
fp = open(filename,"r")
for r in fp.readlines():
    print(json.loads(r))
fp.close()
