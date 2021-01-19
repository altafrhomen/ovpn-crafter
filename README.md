# Ovpn-crafter
Python Program to craft .ovpn file for client Authentication for Openvpn. configuration files: ca.crt, <"clientname">.crt, <"clientname">.key, (optional)tls-crypt.key or tls-auth.key and the pythonscript should be on same directory. If the server is configured with encryption you must include tls-*.key to craft a working .ovpn file.

tls-*.key can be tls-auth.key or tls-crypt.key it depends on how you configured your system for encryption.

**Edit header file**
Replace `xx.xx.xxx.xxx mm ` with your server ip address and port number eg: 10.25.158.36 5000 or example.com 5000

collect the configuration files and keep it together with the python code.

    from ovpn-crafter import Crafter
    
    filename="<output file name>"
    clientcrt="<client certificate file name>"
    clientkey="<client key file name>"
    tls="<tls-*.key>"
    type=<tls-auth or tls-crypt>
    
    moment=crafter(filename)
    moment.ca_cert("ca.crt")
    moment.cl_cert(clientcrt)
    moment.cl_key(clientkey)
    moment.tls(tls,type)
    moment.craft()
    
If your server is not encrypted then avoid tls-*.key and use this code:

    from ovpn-crafter import Crafter
    
    filename="<output file name>"
    clientcrt="<client certificate file name>"
    clientkey="<client key file name>"
    
    moment=crafter(filename)
    moment.ca_cert("ca.crt")
    moment.cl_cert(clientcrt)
    moment.cl_key(clientkey)
    moment.craft()

   
Ovpn files will be generated with the name you gave in filename eg:**Rambo.ovpn**

      
