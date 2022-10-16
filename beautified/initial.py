tmp = eval.__self__
in_script = tmp.__dir__()
minus_ten = -sorted(str(tmp.copyright)[:]).index(" ")
print(minus_ten)

print(tmp.__dict__[in_script[minus_ten]].__name__)

#TODO: last line .__.