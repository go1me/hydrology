import numpy as np


def rai(datanp):
  '''
  计算rai，参考R语言
  https://github.com/lucasvenez/precintcon/blob/master/R/precintcon.rai.analysis.r
  '''
	sort_datanp = datanp.copy()
	sort_datanp.sort()

	xb = sort_datanp[0:10].mean()
	mb = sort_datanp[-10:].mean()
	k = datanp.mean()

	for i in range(len(datanp)):
		x = datanp[i]
		if x < k:
			datanp[i] = -3 * ((x - k) / (xb - k))
		else:
			datanp[i] = 3 * ((x - k) / (mb - k))
	return datanp


datanp = np.arange(200)

print(rai(datanp))

	
