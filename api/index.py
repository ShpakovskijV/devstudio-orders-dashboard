from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import csv, io, json, os

class handler(BaseHTTPRequestHandler):
 def do_GET(self):
  try:
   with open(os.path.join(os.path.dirname(__file__),'..','sample_orders.csv'),encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
   orders=[]
   for row in rows:
    q=int(row['quantity']); p=float(row['unit_price'])
    if q<0 or p<0: raise ValueError('Negative value')
    orders.append(dict(order_id=row['order_id'],customer=row['customer'],total=round(q*p,2),status=row['status']))
   status=parse_qs(urlparse(self.path).query).get('status',[''])[0].lower()
   if status: orders=[o for o in orders if o['status'].lower()==status]
   data=dict(orders=orders,count=len(orders),revenue=round(sum(o['total'] for o in orders if o['status'].lower()=='paid'),2))
   body=json.dumps(data).encode()
   self.send_response(200)
  except Exception as e:
   body=json.dumps({'error':str(e)}).encode(); self.send_response(500)
  self.send_header('Content-Type','application/json; charset=utf-8')
  self.send_header('Content-Length',str(len(body)))
  self.end_headers(); self.wfile.write(body)
