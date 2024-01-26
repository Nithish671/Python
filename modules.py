import myModule as mx
import platform

mx.greeting("Itachi")

print(mx.person["eyeColor"])
i = mx.person["eyeColor"]
print(i)

x = platform.system()
print(x)

y = dir(platform)
print(y)

z = dir(mx)
print(z)