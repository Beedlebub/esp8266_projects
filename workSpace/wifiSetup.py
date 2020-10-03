def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ORBI11', 'Eyel0veNYC')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
do_connect()

