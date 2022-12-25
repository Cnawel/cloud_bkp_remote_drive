from ftp_conn import ftp_conn_main
from ftp_conn import ftp_host, ftp_user, ftp_pass
import urllib.request 

ftp = ftp_conn_main()

#### OPT 1
# import urllib.request

#urllib.request.urlretrieve('ftp://server/path/to/file', 'file')
# if you need to pass credentials:
urllib.request.urlretrieve(f'ftp://{ftp_user}:{ftp_pass}@{ftp_host}/user_backups/2022-14-07/', 'bizki602.tar.gz')

# ### OPT 2
# import shutil
# import urllib.request
# from contextlib import closing

# with closing(urllib.request.urlopen(f'ftp://{ftp_host}@{ftp_user}/user_backups/2022-12-07')) as r:
#     with open('bizki602.tar.gz', 'wb') as f:
#         shutil.copyfileobj(r, f)

### PYTHON 2 OPT 3
# import shutil
# import urllib2
# from contextlib import closing

# with closing(urllib2.urlopen('ftp://server/path/to/file')) as r:
#     with open('file', 'wb') as f:
#         shutil.copyfileobj(r, f)