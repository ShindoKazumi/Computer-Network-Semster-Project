from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

class ProjectTopo( Topo ):

	def build( self ):

		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )

		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		
		self.addLink( h1, s1 )
		self.addLink( s1, h2 )
		self.addLink( h2, s2 )
		self.addLink( s2, h3 )
		self.addLink( h3, s3 )
		self.addLink( s3, h1 )
		self.addLink( h1, s3 )

def runProjectTopo():
	
	topo = ProjectTopo()

	net = Mininet(
		topo = topo,
		controller = lambda name: RemoteController( name, ip= '192.168.176.3' ),
		switch = OVSSwitch,
		autoSetMacs = True )

	net.start()

	CLI( net )

	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	runProjectTopo()
