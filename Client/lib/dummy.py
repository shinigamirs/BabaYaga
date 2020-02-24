import time
import sys

for i in range(0, 100):
  print(i)
  sys.stdout.flush() # flushes stdout to be read by parent js process
  time.sleep(1.0)