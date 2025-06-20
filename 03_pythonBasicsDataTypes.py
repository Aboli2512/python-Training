#text type: str
#numeric types: int,float,complex
# sequence types: list, tuple,
# rangemapping types: dict
# set types:set, frozen set
# boolean types: bool 
# binary types: bytes, bytearray, memoryview 
# none type: none type

#data types
print(type("Hello World"),
      type(20),
      type(20.5),
      type(1j),
      type(['apple', 'banana']),
      type(('apple', 'banana')),
      type(range(6)),
      type({"name" : "john", "age" : 36}),
      type(frozenset({'apple', 'banana'})),
      type(True),
      type(None)
      )

x = b"Hello"
y = bytearray(5)
z = memoryview(bytes(5))
print(x, y, z)
print(type(x), type(y), type(z))

# input fuction

a = int(input('enter vale of a'))
b = int(input('enter value of b'))
print('number ia a', a)
print( 'number is b', b)
print( 'sum is' , a + b)