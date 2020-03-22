from hashlib import sha256
doc = 'GAYPS6180K'
print(sha256(doc.encode()).hexdigest())
