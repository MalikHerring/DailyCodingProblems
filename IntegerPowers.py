def intpow(base, power):
	if power is 0:
		return 1
	if power is 1:
		return base
	if (power & 1) is not 0:
		return base * intpow(base * base, power // 2)
	else:
		return intpow(base * base, power // 2)
