# -*- coding: UTF-8 -*-
import datetime
import simplejson as json
import redis
abcd={"imageNum": 0, "pv": 0, "ctr": 0, "level": 0, "url": u"http://www.puahome.com/bbs/pua-91734-1-1.html", "len": 7938, "sumImage": 7, "pn": 0, "id": 96095L}
abc = json.dumps(abcd)
r = redis.Redis(host='localhost', port=6379, db=0)
r.hset('test', 12345666, abcd)
hello = r.hget('test', 12345666)
abcdef = eval(hello)
exec ("c=" + a)
print type(abcdef)
'''
ret_dict = json.loads(abc, "UTF-8")
print ret_dict
'''