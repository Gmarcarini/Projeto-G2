import random
from classes import barbaro, bardo, mago, ladino, paladino, plebeu1, plebeu2, ajudante, paladino2

class AnaoMontanha:
    def __init__(self, classe):
        self.nome = 'Anao da Montanha'
        d4 = [random.randint(1,4) for i in range(5)]
        d6 = [random.randint(1,6) for i in range(1)]
        self.altura = 1.22 + sum(d4)
        self.peso = 65 + (sum(d4) * sum(d6) / 5)
        self.idiomas = ['comum', 'anao']
        self.habilidades = classe.habilidades
        self.habilidades.constituicao += 2
        self.habilidades.forca += 2
        self.proef = ['armaduras leves', 'armaduras medias', 'machados de batalha', 'machadinhas', 'martelos leves', 'martelos de guerra']
        self.deslocamento = 7.5
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.'
            }
        self.classe = classe

class AnaoColina:
    def __init__(self, classe):
        self.nome = 'Anao da Colina'
        d4 = [random.randint(1,4) for i in (range(5))]
        d6 = [random.randint(1,6) for i in (range(1))]
        self.altura = 1.12 + sum(d4)
        self.peso = 57 + (sum(d4) * sum(d6) / 5)
        self.idiomas = ['comum', 'anao']
        self.habilidades = classe.habilidades
        self.habilidades.constituicao += 2
        self.habilidades.sabedoria += 1
        self.proef = ['machados de batalha', 'machadinhas', 'martelos leves', 'martelos de guerra']
        self.deslocamento = 7.5
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.'
            }
        self.classe = classe

class AltoElfo:
    def __init__(self, classe):
        self.nome = 'Alto Elfo'
        d10 = [random.randint(1,10) for i in (range(5))]
        d4 = random.randint(1,4)
        self.altura = 1.37 + sum(d10)
        self.peso = 45 + (sum(d10) * d4 / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.inteligencia += 1
        self.deslocamento = 9
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            'Sentidos Aguçados': 'Você tem proficiência na perícia Percepção.',
            'Transe': 'Elfos podem entar em transe (meditação) para descansar durante 4 horas, equivate a um descanso de 8 horas'
            }
        self.proef = ['espadas longas', 'espadas curtas', 'arcos longos', 'arcos curtos']
        self.truques = []
        self.classe = classe


class ElfoFloresta:
    def __init__(self, classe):
        self.nome = 'Elfo da Floresta'
        d10 = [random.randint(1,10) for i in (range(5))]
        d4 = random.randint(1,4)
        self.altura = 1.37 + sum(d10)
        self.peso = 50 + (sum(d10) * d4 / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.sabedoria += 1
        self.deslocamento = 10.5
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            'Sentidos Aguçados': 'Você tem proficiência na perícia Percepção.',
            'Transe': 'Elfos podem entar em transe (meditação) para descansar durante 4 horas, equivate a um descanso de 8 horas',
            'Mascara da natureza': 'Voce pode tentar se esconder mesmo quando esta apenas levemente obscurecido'
            }
        self.proef = ['espadas longas', 'espadas curtas', 'arcos longos', 'arcos curtos']
        self.classe = classe

class ElfoNegro:
    def __init__(self, classe):
        self.nome = 'Elfo Negro'
        d6 = [random.randint(1,6) for i in (range(5))]
        d_6 = random.randint(1,6)
        self.altura = 1.32 + sum(d6)
        self.peso = 48 + (sum(d6) * sum(d_6) / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.carisma += 1
        self.deslocamento = 10.5
        self.caract_raca = {
            'Visão no escuro superior': 'enxerga na penumbra a até 36 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            'Sentidos Aguçados': 'Você tem proficiência na perícia Percepção.',
            'Transe': 'Elfos podem entar em transe (meditação) para descansar durante 4 horas, equivate a um descanso de 8 horas',
            'Mascara da natureza': 'Voce pode tentar se esconder mesmo quando esta apenas levemente obscurecido',
            'Sensibilidade a luz solar': 'Voce possui desvantagem em testes de percepcao se o alvo esta sob luz solar direta'
            }
        self.proef = ['rapieiras', 'espadas curtas', 'bestas de mao']
        self.classe = classe

class HalflingPesLeves:
    def __init__(self, classe):
        self.nome = 'Halfling Pés Leves'
        d6 = [random.randint(1,6) for i in (range(5))]
        self.altura = 0.78 + sum(d6)
        self.peso = 18 + (sum(d6) * 1 / 5)
        self.idiomas = ['comum', 'halfling']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.carisma += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Sortudo': 'Se voce tirar 1 natural, voce pode rolar de novo e utilizar o novo resultado da rolagem',
            'Agilidade Halfling': 'Voce pode se mover atraves do espaço de qualquer criatura que for de um tamanho maior que o seu',
            'Furtividade Natural': 'Voce pode tentar se esconder mesmo quando possuir apenas uma cobertura de uma criatura que for no minimo um tamanho maior que o seu',
            }
        self.classe = classe

class HalflingRobusto:
    def __init__(self, classe):
        self.nome = 'Halfling Robusto'
        d6 = [random.randint(1,6) for i in (range(5))]
        self.altura = 0.78 + sum(d6)
        self.peso = 18 + (sum(d6) * 1 / 5)
        self.idiomas = ['comum', 'halfling']
        self.habilidades = classe.habilidades
        self.habilidades.destreza += 2
        self.habilidades.constituicao += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Sortudo': 'Se voce tirar 1 natural, voce pode rolar de novo e utilizar o novo resultado da rolagem',
            'Bravura': 'Voce tem vantagem em testes de resistencia contra ficar amedrontado',
            'Agilidade Halfling': 'Voce pode se mover atraves do espaço de qualquer criatura que for de um tamanho maior que o seu',
            }
        self.classe = classe

class Humano:
    def __init__(self, classe):
        self.nome = 'Humano'
        d10 = [random.randint(1,10) for i in (range(5))]
        d4 = [random.randint(1,4) for i in (range(1))]
        self.altura = 1.42 + sum(d10)
        self.peso = 55 + (sum(d10) * sum(d4) / 5)
        self.idiomas = ['comum']
        self.habilidades = classe.habilidades
        self.habilidades.forca += 1
        self.habilidades.destreza += 1
        self.habilidades.constituicao += 1
        self.habilidades.inteligencia += 1
        self.habilidades.sabedoria += 1
        self.habilidades.carisma += 1
        self.deslocamento = 9  
        self.classe = classe

class Draconato:
    def __init__(self, classe):
        self.nome = 'Draconato'
        d8 = [random.randint(1,8) for i in (range(5))]
        d6 = [random.randint(1,6) for i in (range(1))]
        self.altura = 1.67 + sum(d8)
        self.peso = 87 + (sum(d8) * sum(d6) / 5)
        self.idiomas = ['comum', 'draconico']
        self.habilidades = classe.habilidades
        self.habilidades.forca += 2
        self.habilidades.carisma += 1
        self.deslocamento = 9
        d10 = random.randint(1,10)
        ancestrais = {'Azul': 'Elétrico, Linha de 1,5 a 9m, teste de destreza',
                      'Branco': 'Frio, cone de 4,5m, teste de constituicao',
                      'Bronze': 'Eletrico, Linha de 1,5 a 9m, teste de destreza',
                      'Cobre': 'Acido, Linha de 1,5 a 9m, teste de destreza',
                      'Latao': 'Fogo, Linha de 1,5 a 9m, teste de destreza',
                      'Negro': 'Acido, Linha de 1,5 a 9m, teste de destreza',
                      'Ouro': 'Fogo, Cone de 4,5m , teste de destreza',
                      'Prata': 'Frio, Cone de 4,5m, teste de constituicao',
                      'Verde': 'Veneno, Cone de 4,5m, teste de constituicao',
                      'Vermelho': 'Fogo, Cone de 4,5m, teste de destreza'
                      }
        for i, (chave, valor) in enumerate(ancestrais.items(), start=1):
            if i == d10:
                self.ancestral = {chave: valor}
                break
        self.classe = classe

class GnomoFloresta:
    def __init__(self, classe):
        self.nome = 'Gnomo da floresta'
        d4 = [random.randint(1,4) for i in (range(5))]
        self.altura =0.88 + sum(d4)
        self.peso = 18 + (sum(d4) * 1 / 5)
        self.idiomas = ['comum', 'gnomico']
        self.habilidades = classe.habilidades
        self.habilidades.inteligencia += 2
        self.habilidades.destreza += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            'Falar com bestas pequenas': 'atraves de sons e gestos voce consegue comunicar ideias simples para bestas pequenas ou menores'
            }
        self.truques = ['ilusao pequena']
        self.classe = classe

class GnomoRochas:
    def __init__(self, classe):
        self.nome = 'Gnomo das Rochas'
        d4 = [random.randint(1,4) for i in (range(5))]
        self.altura =0.88 + sum(d4)
        self.peso = 18 + (sum(d4) * 1 / 5)
        self.idiomas = ['comum', 'gnomico']
        self.habilidades = classe.habilidades
        self.habilidades.inteligencia += 2
        self.habilidades.constituicao += 1
        self.deslocamento = 7.5  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            'Conhecimento artificie': 'Se realizar um teste de inteligencia historia, referente a itens magicos, objetos alquimicos ou mecanismos tecnologicos voce adiciona o dobro de do seu bonus de proeficiencia ',
            'Engenhoqueiro': 'Voce pode gastar 1 hora e 10 po para criar um mecanismo miúdo(CA 5, 1pv) e pode ter até 3 desses mecanismos ativos ao memso tempo, ele dura 24 horas'
            }
        self.truques = ['ilusao pequena']
        self.proef = ['ferramentas de artesao']
        self.classe = classe

class MeioElfo:
    def __init__(self, classe):
        self.nome = 'Meio Elfo'
        d8 = [random.randint(1,8) for i in (range(5))]
        d4 = [random.randint(1,4) for i in (range(1))]
        self.altura = 1.45 + sum(d8)
        self.peso = 55 + (sum(d8) * sum(d4) / 5)
        self.idiomas = ['comum', 'elfico']
        self.habilidades = classe.habilidades
        self.habilidades.carisma += 2
        self.habilidades.destreza += 1
        self.habilidades.sabedoria += 1
        self.deslocamento = 9  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            }
        self.classe = classe

class MeioOrc:
    def __init__(self, classe):
        self.nome = 'Meio Orc'
        d8 = [random.randint(1,8) for i in (range(5))]
        d6 = [random.randint(1,6) for i in (range(1))]
        self.altura = 1.47 + sum(d8)
        self.peso = 70 + (sum(d8) * sum(d6) / 5)
        self.idiomas = ['comum', 'orc']
        self.habilidades = classe.habilidades
        self.habilidades.forca += 2
        self.habilidades.constituicao += 1
        self.deslocamento = 9  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            'Ataques selvagens': 'Quando atingir um ataque critico com uma arma corpo a corpo, voce rola mais um dado de dano da arma para dar dano extra'
            }
        self.proef = ['intimidacao']
        self.classe = classe

class Tieflings:
    def __init__(self, classe):
        self.nome = 'Tiefling'
        d8 = [random.randint(1,8) for i in (range(5))]
        d4 = [random.randint(1,4) for i in (range(1))]
        self.altura = 1.45 + sum(d8)
        self.peso = 55 + (sum(d8) * sum(d4) / 5)
        self.idiomas = ['comum', 'infernal']
        self.habilidades = classe.habilidades
        self.habilidades.inteligencia += 1
        self.habilidades.carisma += 2
        self.deslocamento = 9  
        self.caract_raca = {
            'Visão no escuro': 'enxerga na penumbra a até 18 metros como se fosse luz pa, e no escuro como se fosse na penumbra.',
            }
        self.truques = ['traumaturgia']
        self.classe = classe

anao_montanha = AnaoMontanha(barbaro)
meio_elfo = MeioElfo(bardo)
gnomo_floresta = GnomoFloresta(ladino)
tieflings = Tieflings(mago)
draconato = Draconato(paladino)
dono_bar = AnaoColina(plebeu1)
bebado = MeioOrc(plebeu2)
ajudante = Humano(ajudante)
reginald = Humano(paladino2)