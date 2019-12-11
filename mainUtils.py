
class mainUtils(object):

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def gravar(dados):
        arquivo = open('metafeatures_output.txt','w')
        arquivo.write(dados)
        arquivo.close()    
