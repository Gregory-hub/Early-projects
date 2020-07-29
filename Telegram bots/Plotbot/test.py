import matplotlib.pyplot as plt


xs = [i/3 for i in range(-90, 91)]


def get_xs_ys(x0, fun: str):
	ys_temp, xs_temp = [], []
	ys, xs = [], []
	for x in x0:
		try:
			ys_temp.append(eval(fun))
			xs_temp.append(x)
		except:
			ys.append(ys_temp)
			xs.append(xs_temp)
			ys_temp, xs_temp = [], []
			continue
	if len(xs) == 0:
		xs = xs_temp
		ys = ys_temp
	return xs, ys


fun = "1/x"
xs, ys = get_xs_ys(xs, fun)

plt.style.use('fivethirtyeight')



plt.plot(xs, ys, color='gray')

plt.show()