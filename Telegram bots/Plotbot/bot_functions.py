def get_xs_ys():
	xs = [i/3 for i in range(-30, 31)]
	i = 0
	n = len(xs)
	ys = []
	while i < n:
		x = xs[i]
		try:
			ys.append(eval(fun))
		except:
			xs.pop(i)
			n = len(xs)
			continue
		n = len(xs)
		i += 1
	return xs, ys