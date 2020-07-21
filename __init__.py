class A():

    oss_url = 'g.cn/?'

    @property
    def oss_url(self):
        print(dir(a)['oss_url'])
        return self.oss_url + '&signture=1'

    @oss_url.setter
    def oss_url(self, values):
        self._oss_url = values
        return self._oss_url


a = A()
print(a.oss_url)

