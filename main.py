country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=0
network={
  ssid="eduroam"
  identity="CHANGE TO_YOUR_USERNAME@umd.edu"
  password="CHANGE_TO_YOUR_PASSWORD"
  key_mgmt=WPA-EAP
  eap=PEAP
  phase1="peaplabel=0"
  phase2="auth=MSCHAPV2"
  disabled=0
  mode=0
  auth_alg=OPEN
  proto=WPA RSN
  proactive_key_caching=1
}