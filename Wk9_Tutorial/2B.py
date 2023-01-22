# Print date and time together in the form of : mm/dd/yyyy hh:mm:sss
# / For this use datetime class of datetime module [From import method]
# // Hint use %s%s%s %s:%s:%s

import datetime
datetime_obj = datetime.datetime.now()
print(datetime_obj)

from datetime import datetime
datetime_ddmmyyyy = datetime.day, datetime.month, datetime.year
datetime_hrmm = datetime

# print("%s%s%s %s:%s:%s" , datetime_ddmmyyyy, datetime_hrmm)
print(datetime_ddmmyyyy,datetime_hrmm, '%s%s%s %s:%s:%s')