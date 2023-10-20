# -*- coding: utf-8 -*-


class TabelaHash:
    def __init__(self, tamanho_n):
        
        self.primeiro_nivel = [None] * 10
        for i in range(10):
            self.primeiro_nivel[i] = [None] * (tamanho_n // 10)

    def hash_primeiro_nivel(self, chave):
        
        return hash(chave) % 10

    def hash_segundo_nivel(self, chave):
        
        return hash(chave) % (len(self.primeiro_nivel[0]))

    def inserir(self, chave, valor):
        primeiro_hash = self.hash_primeiro_nivel(chave)
        segundo_hash = self.hash_segundo_nivel(chave)
        
        if self.primeiro_nivel[primeiro_hash][segundo_hash] is None:
            self.primeiro_nivel[primeiro_hash][segundo_hash] = []
        
        self.primeiro_nivel[primeiro_hash][segundo_hash].append((chave, valor))

    def buscar(self, chave):
        primeiro_hash = self.hash_primeiro_nivel(chave)
        segundo_hash = self.hash_segundo_nivel(chave)

        if self.primeiro_nivel[primeiro_hash][segundo_hash] is not None:
            for c, v in self.primeiro_nivel[primeiro_hash][segundo_hash]:
                if c == chave:
                    return v
        return None

