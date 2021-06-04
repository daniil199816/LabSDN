
#!/usr/bin/python
from mininet.topo importTopo
from mininet.net importMininet
from mininet.node importCPULimitedHost
from mininet.link importTCLink
from mininet.util importirange,dumpNodeConnections
from mininet.log importsetLogLevel
classLinearTopo(Topo):
"Linear topology of k switches, with one host per switch."
def__init__(self, k=2, **opts):
"""Init.
k: number of switches (and hosts)
hconf: host configuration options
lconf: link configuration options"""
super(LinearTopo, self).__init__(**opts)
self.k =k
lastSwitch =None
fori inirange(1, k):
host =self.addHost('h%s' %i, cpu=.5/k)
switch =self.addSwitch('s%s' %i)
# 10 Mbps, 5ms delay, 1% loss, 1000 packet queue
self.addLink( host, switch, bw=10, delay='5ms', loss=1,
max_queue_size=1000, use_htb=True)
iflastSwitch:
self.addLink(switch, lastSwitch, bw=10, delay='5ms', loss=1,
max_queue_size=1000, use_htb=True)
lastSwitch =switch
defperfTest():
"Create network and run simple performance test"
topo =LinearTopo(k=4)
net =Mininet(topo=topo,
host=CPULimitedHost, link=TCLink)
net.start()
print"Dumping host connections"
dumpNodeConnections(net.hosts)
print"Testing network connectivity"
net.pingAll()
print"Testing bandwidth between h1 and h4"
h1, h4 =net.get('h1', 'h4')
net.iperf((h1, h4))
net.stop()
if__name__ =='__main__':
setLogLevel('info')
perfTest()
