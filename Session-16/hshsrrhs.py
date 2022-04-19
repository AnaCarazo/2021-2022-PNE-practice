text = "http://localhost:63342/operation?seq=AACC&operation=Info"
seq = text.split("?seq=")[1].split("&")[0]
operation = text.split("&operation=")[1]
print(seq, operation)