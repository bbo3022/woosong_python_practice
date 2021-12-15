def print_kwargs(**kwargs):
	Keys=kwargs.keys()
	Values=kwargs.values()
	Items=kwargs.items()
	print(kwargs)
	print(Keys)
	print(Values)
	print(Items)

print_kwargs(a=1)
print_kwargs(name="foo", age=3)