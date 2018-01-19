import os
import json
import urllib2
import StringIO
import gzip

server = os.environ.get('EVE_SERVER', "TQ")
version = os.environ.get('VERSION_EVE', "latest")
if version == "latest":
    content = urllib2.urlopen("http://binaries.eveonline.com/eveclient_%s.json" % server).read().decode()
    version = json.loads(content)['build']

content = urllib2.urlopen("http://binaries.eveonline.com/eveonline_%s.txt" % version).read().decode()
for line in content.split("\r\n"):
    if line == "":
        continue
    local, remote, _, _, _, _ = line.split(",")
    local = local.replace("app:/", "")
    # TODO: should check hash / size from the index if you change version and have files stored permanently
    if os.path.exists(local):
        continue
    url = urllib2.urlopen("https://binaries.eveonline.com/%s" % remote)
    try:
        os.makedirs(os.path.dirname(local))
    except:
        pass
    with open(local, 'wb') as f:
        raw = url.read()
        try:
            data = gzip.GzipFile(fileobj=StringIO.StringIO(raw)).read()
        except:
            data = raw
        f.write(data)
