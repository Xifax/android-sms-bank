# coding: utf-8

import nmap

from smsbank.apps.hive.models import Device


class Scanner:
    """
    SMS Hive scanner.
    Discovers android devices with capability
    to process requests from HiveMind.
    """

    def __init__(self):
        self.check_url = 'status'
        self.valid_response = 'SMS-GRUNT'

    def scan(
        self,
        network='192.168.1.0/24',
        port=8080,
        additional_check=False,
        persist=False
    ):
        """Scan network for android sms grunts"""
        grunts = []
        # Scan specified network
        scanner = nmap.PortScanner()
        scanner.scan(network, str(port))

        # Check all the found hosts
        for host in scanner.all_hosts():
            if scanner[host]['tcp'][port]['state'] == 'open':
                grunts.append(host)
                # TODO: if required, try to GET '/status' for additional check

        # Update devices in DB
        if(persist):
            for grunt in grunts:
                try:
                    device = Device.objects.get(ip=grunt)
                    device.online = True
                    device.save()
                except Device.DoesNotExist:
                    device = Device(ip=grunt, online=True)
                    device.save()

        return grunts
