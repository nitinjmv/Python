
def rev(s):
    rs = "";
    for k in s:
        rs = k + rs
    return rs

s = "hello world"
print(rev(s))