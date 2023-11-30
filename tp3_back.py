from random import choice

class PPT:
    opciones = ['piedra', 'papel', 'tijera']

    #ultimo_ganador = None
    #txt = ""
    puntaje_us=0
    puntaje_pc=0

    def pc_juega(self):
        return choice(PPT.opciones)
    
    def ganador_player(self, player, pc):
        if (player== self.opciones[0] and pc==self.opciones[2]) or(player==self.opciones[1] and pc==self.opciones[0]) or(player==self.opciones[2] and pc==self.opciones[1]):
            PPT.puntaje_us+=1
            return True
        else:
            PPT.puntaje_pc+=1
            return False
        
    def empate(self, player, pc):
        return player == pc    

    def jugar(self, mi_opcion):
        jugada_pc = self.pc_juega()
        
        if self.ganador_player(mi_opcion, jugada_pc):
            return "¡GANASTE! Felicitaciones"
        elif self.empate(mi_opcion, jugada_pc):
            return "¡EMPATAMOS!. Vamos a jugar otra vez."
        else:
            print(f"vos: {mi_opcion} - yo: {jugada_pc}")
            return "¡PERDISTE!. Yo gané"


    def jugar_con_piedra(self):
        return self.jugar(PPT.opciones[0])

    def jugar_con_papel(self):
        return self.jugar(PPT.opciones[1])

    def jugar_con_tijera(self):
        return self.jugar(PPT.opciones[2])
    
    def puntaje(self):
        print(f"User: {self.puntaje_us}\nPC: {self.puntaje_pc}")