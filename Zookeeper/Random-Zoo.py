
from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
def my_listener(state):
  if state == KazooState.LOST:
    print("Lost")
  elif state == KazooState.SUSPENDED:
    print("Suspended")
  else:
    print("Connected")

def my_func(event):
  print ("node status has changed")

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
print("Connection strted")
zk.add_listener(my_listener)

# Determine if a node exists
if zk.exists("/tester"):
  print("tester exists")
# Print the version of a node and its data
#data, stat = zk.get("/my/favorite")
#print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

# List the children
children = zk.get_children("/tester",watch=my_func)
print("There are %s children with names %s" % (len(children), children))
for i in children:
    zk.set('/tester/test1', b"some data")
time.sleep(500)
