import re


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, url):
        pattern = '[^ /\f\n\r\t\v\.]+\.[^ /\f\n\r\t\v\.\+]+'
        if re.fullmatch(pattern, url):
            self.url = url
        else:
            raise DomainException('Недопустимый домен, url или email')

    def __str__(self):
        return self.url
    @classmethod
    def from_url(cls,url):
        if url.startswith("https://") or url.startswith("http://"):
            _, s = url.split('//')
            return cls(s)
        raise DomainException('Недопустимый домен, url или email')
    @classmethod
    def from_email(cls, url):
        if re.search('\w@{1,1}',url) and not re.search('_+|,+',url):
            try:
                s = url.split('@')
                if len(s)==2:
                    return cls(s[1])
            except:
                raise DomainException('Недопустимый домен, url или email')
        raise DomainException('Недопустимый домен, url или email')

emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org', 'abc@@mail.ru',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
        print(email)
    except DomainException as e:
        pass


domain1 = Domain('pygen.ru')
domain2 = Domain.from_url('https://pygen.ru')
domain3 = Domain.from_email('support@pygen.ru')

print(domain1)
print(domain2)
print(domain3)