#!/usr/bin/env python

from pprint import pprint
from bluetooth import *

def find_devices():
	print "performing inquiry..."

	nearby_devices = discover_devices(lookup_names = True, flush_cache = True, duration = 20)

	print "found %d devices" % len(nearby_devices)

	for name, addr in nearby_devices:
	     print " %s - %s" % (addr, name)


def find_by_name():
	target_name = "G4"
	target_address = None

	nearby_devices = discover_devices(lookup_names = True, flush_cache = True, duration = 20)

	for name, addr in nearby_devices:
	    if target_name == lookup_name( name ):
		target_address = bdaddr
		break

	if target_address is not None:
	    print "found target bluetooth device with address ", target_address
	else:
	    print "could not find target bluetooth device nearby"

def get_service():
	services = find_service(address='DC:0B:34:71:36:85')
	if 0 == len( services ):
		print "not found"
	else:
		pprint(services)

if __name__ == "__main__":
	get_service()

