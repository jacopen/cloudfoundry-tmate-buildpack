__author__ = 'jacopen'
import json
import os
import re

env = '{"mysql-5.5":[{"name":"mysql-tmate-1","label":"mysql-5.5","tags":["mysql","relational"],"plan":"default","credentials":{"name":"d072a63541426458aa9419604326a36f8","hostname":"153.149.5.25","host":"153.149.5.25","port":3307,"user":"uPV9jCqnOHY2w","username":"uPV9jCqnOHY2w","password":"pBY8c9Fq8GdUP","uri":"mysql://uPV9jCqnOHY2w:pBY8c9Fq8GdUP@153.149.5.25:3307/d072a63541426458aa9419604326a36f8"}},{"name":"mysql-tmate-","label":"mysql-5.5","tags":["mysql","relational"],"plan":"default","credentials":{"name":"d386db34fdae2498aa27e45906602ed5e","hostname":"153.149.5.25","host":"153.149.5.25","port":3307,"user":"uz9251DJAot9K","username":"uz9251DJAot9K","password":"paSkoVplCri7r","uri":"mysql://uz9251DJAot9K:paSkoVplCri7r@153.149.5.25:3307/d386db34fdae2498aa27e45906602ed5e"}}],"postgresql-9.2":[{"name":"postgresql-tmate-1","label":"postgresql-9.2","tags":["relational"],"plan":"default","credentials":{"name":"df825ec2a87014c978759d6b2cd588482","host":"153.149.13.35","hostname":"153.149.13.35","port":5434,"user":"u39ae137935174bcea4e433b9f6b256f3","username":"u39ae137935174bcea4e433b9f6b256f3","password":"p0a8329fcd1454d0093fc466343a228e2","uri":"postgres://u39ae137935174bcea4e433b9f6b256f3:p0a8329fcd1454d0093fc466343a228e2@153.149.13.35:5434/df825ec2a87014c978759d6b2cd588482"}}]}'

env = json.loads(env)

services = []

for key, value in env.iteritems():
    for service in value:
        services.append(service)


for index, service in enumerate(services):
    print "{} {}".format(str(index), service['name'])

print "choose service"
input = raw_input()

selected = services[int(input)]
print "selected {}".format(selected['name'])

credentials = selected['credentials']

if re.match(r'mysql', selected['label']):
    cmd = "mysql -u {} -h {} -P {} -p{} {}".format(credentials['user'], credentials['host'], credentials['port'],credentials['password'], credentials['name'])
elif re.match(r'postgresql', selected['label']):
    cmd = "PGPWSSWD={} psql -U {} -h {} -p {} -d {}".format(credentials['password'], credentials['user'], credentials['host'], credentials['port'], credentials['name'])
else:
    print "Don't support this service type."
    exit()

#print cmd
os.system('top')