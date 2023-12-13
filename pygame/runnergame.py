import pygame
from sys import exit
from random import randint , choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_surf1 = pygame.image.load('pygame/graphics/Player/player_walk_1.png').convert_alpha()#we want the bottom of the rectangle to be as same level as ground so we wrote 300
        player_surf2 = pygame.image.load('pygame/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk =[player_surf1 , player_surf2]
        self.player_index=0 
        self.player_jump = pygame.image.load('pygame/graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect=self.image.get_rect(midbottom=(80,300))
        self.gravity=0
        self.jump_sound=pygame.mixer.Sound('pygame/audio/jump.mp3')
        self.jump_sound.set_volume(0.5)
        
    def player_input(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >=300:
            self.jump_sound.play()
            self.gravity=-20
    
    def apply_gravity(self):
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.bottom >=300:
            self.rect.bottom =300
            
    def animation_state(self):
        if self.rect.bottom<300:
            self.image = self.player_jump
        else :
            self.player_index+=0.1
            if (self.player_index>=len(self.player_walk)):
                self.player_index=0
            self.image=self.player_walk[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self , type):
        super().__init__()
        
        if type =='fly':
            fly1=pygame.image.load('pygame/graphics/Fly/Fly1.png').convert_alpha()
            fly2=pygame.image.load('pygame/graphics/Fly/Fly2.png').convert_alpha()
            self.frames=[fly1 , fly2]
            y_pos = 210
        else :
            snail_frame_1= pygame.image.load('pygame/graphics/snail/snail1.png').convert_alpha()
            snail_frame_2= pygame.image.load('pygame/graphics/snail/snail2.png').convert_alpha()
            self.frames=[snail_frame_1 , snail_frame_2]
            y_pos=300
        
        self.animation_index=0
        self.image=self.frames[self.animation_index]
        self.rect=self.image.get_rect(midbottom = (randint(900,1100 ) , y_pos))
    def animation_state(self):
        self.animation_index+=0.1
        if self.animation_index>=len(self.frames):
            self.animation_index=0
        self.image=self.frames[int(self.animation_index)]
        
    def update(self):
        self.animation_state()
        self.rect.x-=6
        self.destroy()
    def destroy(self):
        if self.rect.x<=-100:
            self.kill()

def display_score():
    current_time=pygame.time.get_ticks()-start_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5
            if obstacle_rect.bottom ==300 :
                screen.blit(snail_image , obstacle_rect)
            else :
                screen.blit(fly_image , obstacle_rect)
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100] 
        return obstacle_list
    else :
        return []

def collisions(player , obstacles) :
    if obstacles :
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect) :
                return False
    return True 
    
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite , obstacle_group  , False):
        obstacle_group.empty()
        return False 
    else :
        return True
def player_animation():
    global player_walker , player_index
    if player_recto.bottom <300:
        player_walker=player_jump
    else:
        player_index+=0.1
        if player_index >= len(player_walk):
            player_index=0
        player_walker=player_walk[int(player_index)]
pygame.init()
screen = pygame.display.set_mode((800 ,400))
pygame.display.set_caption("RUNNER")
game_active=True
clock = pygame.time.Clock()

high_score=0

#GROUPS 
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group=pygame.sprite.Group()

#CLOUDS 
cloud1s=pygame.image.load('pygame/graphics/clouds.png')
cloud1s_scaled = pygame.transform.scale(cloud1s , (120,50))
cloud1s_rect = cloud1s_scaled.get_rect(midbottom=(490,140))

cloud2s=pygame.image.load('pygame/graphics/clouds.png')
cloud2s_scaled = pygame.transform.scale(cloud2s , (120,50))
cloud2s_rect = cloud2s_scaled.get_rect(midbottom=(100,190))

#BUSHES
bush1=pygame.image.load('pygame/graphics/bushes/Bushes1/Bush1_3.png')
bush1_rect=bush1.get_rect(midbottom=(400,300))


#ROCKS 
rock1=pygame.image.load('pygame/graphics/rocks/canyon_rocks/canyon_rock3.png')
rock1_rect=rock1.get_rect(midbottom=(600,300))
#TREES

#SKY
sky_surface=pygame.image.load('pygame/graphics/Sky.png').convert()

#GROUND
ground_surface=pygame.image.load('pygame/graphics/ground.png').convert()

#GAME TITLE
text_font = pygame.font.Font('pygame/font/Pixeltype.ttf', 60)
score_surf = text_font.render('runner' , False , (64,64,64) )
score_rect = score_surf.get_rect(center=(400,50))

#GAME NAME 
game_name=text_font.render('PIXEL RUNNER' ,True, (111 , 196 , 169))
game_name_rect=game_name.get_rect(center=(400,50))



#GAME MESSAGE 
game_message=text_font.render('PRESS SPACE TO RESTART THE GAME' , True , (111 , 196 , 169))
game_message_rect = game_message.get_rect(center=(400,350))

#OBSTACLES 
#SNAIL
snail_frame_1= pygame.image.load('pygame/graphics/snail/snail1.png').convert_alpha()
snail_frame_2= pygame.image.load('pygame/graphics/snail/snail2.png').convert_alpha()
snail_frames =[snail_frame_1 , snail_frame_2]
snail_frame_index =0
snail_image=snail_frames[snail_frame_index]

#FLY
fly_frame_1=pygame.image.load('pygame/graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2=pygame.image.load('pygame/graphics/Fly/Fly2.png').convert_alpha()
fly_frames=[fly_frame_1 , fly_frame_2]
fly_frame_index =0
fly_image =fly_frames[fly_frame_index]


obstacle_rect_list=[]

#PLAYER
player_surf1 = pygame.image.load('pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect=player_surf1.get_rect(midbottom=(80,300))#we want the bottom of the rectangle to be as same level as ground so we wrote 300
player_surf2 = pygame.image.load('pygame/graphics/Player/player_walk_2.png').convert_alpha()
player_walk =[player_surf1 , player_surf2]
player_index=0
player_walker=player_walk[player_index]
player_recto=player_walker.get_rect(midbottom=(80,300))


#JUMPING 
player_jump = pygame.image.load('pygame/graphics/Player/jump.png').convert_alpha()

#PLAYER STANDING
player_stand = pygame.image.load('pygame/graphics/Player/player_stand.png')
player_stand_scaled=pygame.transform.scale(player_stand , (150, 200))
player_stand_rect = player_stand_scaled.get_rect(center=(400,200))


#TIMER 
obstacle_timer=pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 1500)

snail_animation_timer=pygame.USEREVENT +2
pygame.time.set_timer(snail_animation_timer , 300)

fly_animation_timer=pygame.USEREVENT +3
pygame.time.set_timer(fly_animation_timer , 100)


bg_music = pygame.mixer.Sound('pygame/audio/music.wav')
bg_music.set_volume(0.04)
bg_music.play(loops=-1)
start_time=0
player_gravity=0
penalty=0
score =0
collider=False
while True :
    
    if score>high_score:
        high_score=score
    scoring_font=pygame.font.Font('C:/Users/SARVESH/Desktop/vacation projects/pygame/font/Pixeltype.ttf', 40)
    scoring_surf=text_font.render(f'HIGH SCORE: {int(high_score/10)}' ,False , (64,64,64) )
    scoring_rect = scoring_surf.get_rect(center=(640,94))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
        if game_active :
            if event.type == pygame.KEYDOWN:
                if player_recto.bottom==300:
                    if event.key==pygame.K_SPACE:
                        player_gravity=-20
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_recto.bottom==300:
                    if pygame.mouse.get_pressed():
                        player_gravity=-20
        if game_active==False:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                player_gravity=0
                player_recto.bottomleft=(80,300)
                
                start_time=pygame.time.get_ticks()
                score=0
        if game_active:     
            if event.type==obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly' , 'snail' , 'snail' , 'snail'])))
                # if randint(0,2):
                #     new_snail_rect = snail_image.get_rect(midbottom=(randint(900,1100),300))
                #     obstacle_rect_list.append(new_snail_rect)
                # else :
                #     new_fly_rect = fly_image.get_rect(midbottom=(randint(900,1100),210))
                #     obstacle_rect_list.append(new_fly_rect)
            if event.type==snail_animation_timer:
                if snail_frame_index==0: 
                    snail_frame_index=1
                else :
                    snail_frame_index=0
                snail_image=snail_frames[snail_frame_index]
            if event.type==fly_animation_timer:
                if fly_frame_index==0: 
                    fly_frame_index=1
                else :
                    fly_frame_index=0
                fly_image=fly_frames[fly_frame_index]
                
    if game_active :
        cloud1s_rect.left-=4
        if (cloud1s_rect.right<=0):
            cloud1s_rect.left=800
        cloud2s_rect.left-=8
        if (cloud2s_rect.right<=0):
            cloud2s_rect.left=800
        screen.blit(sky_surface , (0,0))
        screen.blit(cloud1s_scaled , cloud1s_rect)
        screen.blit(cloud2s_scaled , cloud2s_rect)
        bush1_rect.left-=3
        if (bush1_rect.right<=0) :
            bush1_rect.left=randint(800,1200)
        rock1_rect.left-=2
        if (rock1_rect.right<=0) :
            rock1_rect.left=randint(1200,1600)
        screen.blit(rock1 , rock1_rect)
        screen.blit(bush1 , bush1_rect)
        screen.blit(ground_surface , (0,300)) #jo upar hai likha hai screen wali layer me wo sabse niche jata hai 
        pygame.draw.rect(screen , '#c0e8ec' , score_rect ,11,10) #10 is the width of the rectangle and 20 is the border radius
        pygame.draw.rect(screen , '#c0e8ec' , score_rect ,11 , 10)
        screen.blit(score_surf , score_rect)
        
        
        # snail_rect.x-=5
        # if (snail_rect.right<=0):
        #     snail_rect.left=800
        # screen.blit(snail_image , snail_rect)
        
        #OBSTACLE MOVEMENT
        #obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        
        # collisions 
        #game_active=collisions(player_recto , obstacle_rect_list)
        
        #player
        player_gravity+=1
        # player_recto.y+=player_gravity
        # if player_recto.bottom>=300:
        #     player_recto.bottom=300
        # player_animation()
        # screen.blit(player_walker, player_recto)
        
        #sprite class
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # player_rect.left+=4
        # if (player_rect.left>=400):
        #     player_rect.x=400
        
        # if !player_rect.colliderect(snail_rect) and snail_rect.right<player_rect.left:
        #     score+=1
        #COLLISIONS
        game_active=collision_sprite()
        score+=1
        screen.blit(scoring_surf, scoring_rect)
    else : 
        obstacle_rect_list.clear()
        player_recto.midbottom=(80,300)
        player_gravity=0
        screen.fill((94 , 129 , 162))
        screen.blit(player_stand_scaled , player_stand_rect)
        screen.blit(game_name , game_name_rect)
        screen.blit(game_message , game_message_rect)
        screen.blit(scoring_surf,scoring_rect)
        bush1_rect.midbottom=(400,300)
        rock1_rect.midbottom=(600,300)
    pygame.display.update()
    clock.tick(60)#this 60 tells the while loop to not run more than 60 times per second 
    
    
    
    