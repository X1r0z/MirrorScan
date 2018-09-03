def assign(service, arg):
	if service == 'www':
		return True, arg

def audit(arg):
	target = arg + '/robots.txt/.php'
	code, head, res, err, _ = curl.curl(target)
	if code == 200:
		if 'User-Agent' in res or 'Disallow' in res or 'Allow' in res:
			security_note('Pathinfo Parse vulnerable: ' + target)
