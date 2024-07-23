import json
import  sys
import  requests
url='https://api.coindesk.com/v1/bpi/currentprice.json'
if len(sys.argv)<2:
     sys.exit("Missing command-line argument")
elif len(sys.argv)==2:
    try:
        n=float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number ")
    try:
        r=requests.get(url)
    except requests.RequestException:
        sys.exit("url not found")

    try:
        j_d=r.json()
    except:
        sys.exit("json list not available")

    rate_float_usd=j_d['bpi']['USD']['rate_float']
    r_f_u=float(rate_float_usd)
    amount=r_f_u*n
    print(f"${amount:,.4f}")
