#Written by Lewin Sorg
#Developer: developermind405@gmail.com
import pygame,ValueHandler,random
pygame.init()
pygame.mixer.init()
bg = pygame.image.load("bg.jpg")
screen = pygame.display.set_mode([bg.get_width(),bg.get_height()])
pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.display.set_caption("Moorhahn")
memory = ValueHandler.Handler.memory()
target1 = pygame.image.load("moorhahn2.png")
pygame.display.set_icon(target1)
activ = True
clock = pygame.time.Clock()
pressed = False
#Coords
#(216, 235)
#(591, 310)
#(39, 329)
#(564, 271)
coords = [(216, 235),(591, 310),(39, 329),(564, 271),(500,271)]
c1 = random.choice(coords)
memory.add(target1,c1)
shoot_sound  = pygame.mixer.Sound("shotgun3.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
target_rect = target1.get_rect()
target_rect.left = c1[0]
target_rect.top = c1[1]
font = pygame.font.Font(None,50)
passiv_delay = 0
state_point = False
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
shell_img2 = pygame.image.load("shell.png")
shell_img2 = pygame.transform.scale(shell_img2,(50,50))
shell_handgun = pygame.image.load("shell_handgun.png")
shell_handgun = pygame.transform.scale(shell_handgun,(50,50))
shell_machinegun = pygame.image.load("machine_shell.png")
shell_machinegun = pygame.transform.scale(shell_machinegun,(60,60))
ammo = 5
ammo_memory = ValueHandler.Handler.memory()
ammo_memory.add("Shotgun",(850,5))
ammo_memory.add("Handgun",(750,12))
ammo_memory.add("Machinegun",(200,40))
ammo_memory.add("Colt",(850,6))
ammo_memory.add("Desert Eagle",(750,12))
point_memory = ValueHandler.Handler.memory()
point_memory.add("Shotgun",5)
point_memory.add("Handgun",2)
point_memory.add("Machinegun",1)
point_memory.add("Colt",4)
point_memory.add("Desert Eagle",3)
sound_handgun = pygame.mixer.Sound("shoot2.wav")
sound_machinegun = pygame.mixer.Sound("shoot.wav")
sound_colt = pygame.mixer.Sound("colt.wav")
sound_eagle = pygame.mixer.Sound("shoot3.wav")
sound_memory = ValueHandler.Handler.memory()
sound_memory.add("Shotgun",(shoot_sound))
sound_memory.add("Handgun",(sound_handgun))
sound_memory.add("Machinegun",(sound_machinegun))
sound_memory.add("Colt",(sound_colt))
sound_memory.add("Desert Eagle",(sound_eagle))
reload_sound = pygame.mixer.Sound("reload.wav")
shoot_sound.set_volume(0.8)
shotgun_img = pygame.image.load("shotgun.png")
handgun_img = pygame.image.load("handung.png")
colt_img = pygame.image.load("colt.png")
colt_img = pygame.transform.scale(colt_img,(90,50))
machinegun_img = pygame.image.load("machinegun.png")
shotgun_img = pygame.transform.scale(shotgun_img,(130,130))
handgun_img = pygame.transform.scale(handgun_img,(80,80))
machinegun_img = pygame.transform.scale(machinegun_img,(130,130))
eagle_img = pygame.transform.scale(pygame.image.load("eagle.png"),(80,80))
current_gun_img = shotgun_img
shell_img = shell_img2
current_index = 0 
shell_sound = pygame.mixer.Sound("shell.wav")
current_name = "Shotgun"
guns = {"Shotgun" : shotgun_img,"Handgun" : handgun_img,"Machinegun" : machinegun_img,"Colt" : colt_img,"Desert Eagle" : eagle_img}
guns_ammo = {"Shotgun" : shell_img2,"Handgun" : shell_handgun,"Machinegun" : shell_machinegun,"Colt" : shell_handgun,"Desert Eagle" : shell_handgun}
font2 = pygame.font.Font(None,30)
points = 0
timer = 180
thetime = 180
dt = 0
old = int(thetime)
passiv_delay2 = 0
shoot_block = False
passiv_delay3 = 0
passiv_delay4 = 0
hold = False
while activ:	
	timer -= dt
 	dt = round(clock.tick(30),2)/10
        thetime -= int(timer - timer - timer / 50)
	minute = thetime/60
	second = thetime-int(thetime/60)*60
	if thetime == 0:
		activ2 = True
		while activ2:
			screen.fill([255,255,255])
			screen.blit(font.render("Your Points: {0}".format(points),1,(0,255,0)),[330,230])
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					activ = False
					activ2 = False
	thetime = 180
	screen.fill([0,0,0])
	screen.blit(bg,[0,0])
	for bird in memory.mem.keys():
		screen.blit(bird,memory.mem[bird])
	if state_point:
		passiv_delay += 1
		screen.blit(point_font,[position[0],position[1]-passiv_delay*2])
		if passiv_delay == 30:
			passiv_delay = 0
			state_point = False

	for i in range(ammo):
		screen.blit(shell_img,(ammo_memory.mem[current_name][0]+int(i*20),470))
	if current_name == "Colt" or current_name == "Handgun" or current_name == "Desert Eagle":
		screen.blit(current_gun_img,[600,0])
	else:
		screen.blit(current_gun_img,[600,-20])
	screen.blit(font2.render(current_name,1,(255,0,0)),[600,50])
	screen.blit(font.render(str(points),1,(0,0,255)),[40,10])
	screen.blit(font.render(str(minute)+":"+str(second),1,(255,0,0)),[450,10])
	pygame.display.flip()
	if shoot_block:
		passiv_delay3 += 1
		shell_sound.play()
		if passiv_delay3 == 20:
			shoot_block = False
			passiv_delay3 = 0
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			activ = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse = event.pos
			if ammo == 0:
				reload_sound.play()
				ammo = ammo_memory.mem[current_name][1]
				if current_name != "Shotgun":
					shoot_block = True
					
				
			else:
				if not shoot_block:
					if current_name == "Shotgun":
						if not pygame.mixer.get_busy():
							sound_memory.mem[current_name].play()
							ammo -= 1
							pygame.draw.circle(screen,(255,0,0),mouse,20)
							pygame.display.flip()
							if target_rect.collidepoint(mouse):
								hit_sound.play()
								point_font = font.render(str("+")+str(point_memory.mem[current_name]),1,(0,255,0))
								screen.blit(point_font,mouse)	
								state_point = True
								old = memory.mem[target1]
								memory.delete(target1)
								c1 = random.choice(coords)
								while c1 == old:
									c1 = random.choice(coords)
								memory.add(target1,c1)
								target_rect.left = c1[0]
								target_rect.top = c1[1]
								position = mouse
								points += point_memory.mem[current_name]
					
					else:
						sound_memory.mem[current_name].play()
						ammo -= 1
						pygame.draw.circle(screen,(255,0,0),mouse,20)
						pygame.display.flip()
						if target_rect.collidepoint(mouse):
							hit_sound.play()
							point_font = font.render(str("+")+str(point_memory.mem[current_name]),1,(0,255,0))
							screen.blit(point_font,mouse)	
							state_point = True
							old = memory.mem[target1]
							memory.delete(target1)
							c1 = random.choice(coords)
							while c1 == old:
								c1 = random.choice(coords)
							memory.add(target1,c1)
							target_rect.left = c1[0]
							target_rect.top = c1[1]
							position = mouse
							points += point_memory.mem[current_name]
											
						if current_name == "Machinegun":
							hold = True


		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				if current_index != len(guns)-1:
					current_index += 1
					current_name = guns.keys()[current_index]
					current_gun_img = guns[guns.keys()[current_index]]
					shell_img   = guns_ammo[guns.keys()[current_index]]
					ammo = ammo_memory.mem[current_name][1]
					reload_sound.play()

			elif event.key == pygame.K_LEFT:
				if current_index != 0:
					current_index -= 1
					current_name = guns.keys()[current_index]
					current_gun_img = guns[guns.keys()[current_index]]
					shell_img   = guns_ammo[guns.keys()[current_index]]
					ammo = ammo_memory.mem[current_name][1]
					reload_sound.play()
		elif event.type == pygame.MOUSEBUTTONUP:
			hold = False
	mouse = pygame.mouse.get_pos()
	if target_rect.collidepoint(mouse):
		pygame.draw.circle(screen,(0,255,0),mouse,13,2)
		pygame.display.flip()
	passiv_delay2 += 1
	if passiv_delay2 == 20:
		old = memory.mem[target1]
		memory.delete(target1)
		c1 = random.choice(coords)
		while c1 == old:
			c1 = random.choice(coords)
		memory.add(target1,c1)
		target_rect.left = c1[0]
		target_rect.top = c1[1]
		position = mouse
		passiv_delay2 = 0
        if hold:
		passiv_delay4 += 1
		if passiv_delay4 >= 1:
			if ammo == 0:
				reload_sound.play()
				ammo = ammo_memory.mem[current_name][1]
				if current_name != "Shotgun":
					shoot_block = True
				
			else:
				if not shoot_block:
					sound_memory.mem[current_name].play()
					ammo -= 1
					pygame.draw.circle(screen,(255,0,0),mouse,20)
					pygame.display.flip()
					if target_rect.collidepoint(mouse):
						hit_sound.play()
						point_font = font.render(str("+")+str(point_memory.mem[current_name]),1,(0,255,0))
						screen.blit(point_font,mouse)	
						state_point = True
						old = memory.mem[target1]
						memory.delete(target1)
						c1 = random.choice(coords)
						while c1 == old:
							c1 = random.choice(coords)
						memory.add(target1,c1)
						target_rect.left = c1[0]
						target_rect.top = c1[1]
						position = mouse
						points += point_memory.mem[current_name]
				
					
				 	passiv_delay4 = 0
					

			

	clock.tick(30)
pygame.quit()
