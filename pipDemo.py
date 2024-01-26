import camelcase

c = camelcase.CamelCase()

txt = "wake up to reality! nothing ever goes as planned in this accursed world"

print(c.hump(txt))