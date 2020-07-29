from mechanize import Browser

br = Browser()
br.open("https://docs.djangoproject.com/en/3.0/topics/auth/default/")

print(br.forms())
