
def first_up(s):
	t = s.lower()
	d = t.split()
	r = []
	for i in d:
		r.append(i.capitalize())
	return ' '.join(r)




