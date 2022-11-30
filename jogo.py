# ===== Inicialização =====
# ----- Importa e inicia pacotes
from pygame import *
from random import *
from config import *
from assets import *
from objetos_e_sprites import *


init()
mixer.init()

# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Flappy Bird')
# Simbolo PyGame
programIcon = image.load('Assets/icone.jpg')
display.set_icon(programIcon)


# ----- Código principal
rodando = True
while rodando:
	window.blit (fundo, (0,0))
	
	if tela_de_inicio:
		velocidade = 0
		bird.movimento_asa ()
		base.update (velocidade)
		
		window.blit (flappy_bird, (40, 50))
	else:
		
		if inicio_jogo and not fim_jogo:
			
			proximo_cano = time.get_ticks()
			if proximo_cano - ultimo_cano >= frequencia_cano:
				y = altura_tela // 2
				posicao_cano = choice(range(-100,100,4))
				altura = y + posicao_cano
				
				top = Cano(window, cano, altura, 1)
				bottom = Cano(window, cano, altura, -1)
				grupo_canos.add(top)
				grupo_canos.add(bottom)
				ultimo_cano = proximo_cano
		
		grupo_canos.update(velocidade)
		base.update(velocidade)	
		bird.update()
		imagem_placar.update(pontuacao)
		
		if sprite.spritecollide(bird, grupo_canos, False) or bird.rect.top <= 0:
			inicio_jogo = False
			if bird.vivo:
				som_impacto.play()
				som_gameover.play()
			bird.vivo = False
			bird.theta = bird.velocidade * -2
	
		if bird.rect.bottom >= altura_tela:
			velocidade = 0
			fim_jogo = True
	
		if len(grupo_canos) > 0:
			c = grupo_canos.sprites()[0]
			if bird.rect.left > c.rect.left and bird.rect.right < c.rect.right and not cano_passado and bird.vivo:
				cano_passado = True
	
			if cano_passado:
				if bird.rect.left > c.rect.right:
					cano_passado = False
					pontuacao += 1
					som_acerto.play()



# ===== Finalização =====
quit()
