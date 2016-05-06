# coding: utf-8

from datetime import date


class Law:
    def __init__(self, year=None, legislature=None, number=None, type=None,
                 kind=None, pub_date=None, title=None, nor=None, url_legi=None,
                 id_legi=None, url_an=None, id_an=None, url_senat=None,
                 id_senat=None):
        self.year = year
        self.legislature = legislature
        self.number = number
        self.type = type
        self.kind = kind
        self.pub_date = pub_date
        self.nor = nor
        self.title = title
        self.url_legi = url_legi
        self.id_legi = id_legi
        self.url_an = url_an
        self.id_an = id_an
        self.url_senat = url_senat
        self.id_senat = id_senat

    def to_json(self):
        d = dict()

        for k, v in self.__dict__.iteritems():
            if v is not None:
                if isinstance(v, date):
                    d[k] = v.isoformat()
                else:
                    d[k] = v

        return d
