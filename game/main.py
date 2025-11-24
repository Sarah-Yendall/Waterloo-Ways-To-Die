#!/usr/bin/env python3
"""Minimal Pygame skeleton for "Waterloo Ways To Die" prototype."""
import sys
import random
import time
import pygame

SCREEN_W, SCREEN_H = 1280, 720
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 30, 30)
BLUE = (50, 150, 255)


def draw_text(surface, text, size, x, y, color=BLACK):
    font = pygame.font.SysFont(None, size)
    t = font.render(text, True, color)
    rect = t.get_rect(center=(x, y))
    surface.blit(t, rect)


class Player:
    def __init__(self):
        self.w = 40
        self.h = 40
        self.rect = pygame.Rect(SCREEN_W // 2 - self.w // 2, SCREEN_H - 100, self.w, self.h)
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(SCREEN_W - self.w, self.rect.x))

    def draw(self, surf):
        pygame.draw.rect(surf, BLUE, self.rect)


class Obstacle:
    def __init__(self):
        self.w = 30
        self.h = 30
        self.x = random.randint(0, SCREEN_W - self.w)
        self.y = -self.h
        self.speed = random.uniform(3, 6)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.rect.y += self.speed

    def draw(self, surf):
        pygame.draw.rect(surf, RED, self.rect)


def title_screen(screen, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        screen.fill(WHITE)
        draw_text(screen, "Waterloo Ways To Die", 48, SCREEN_W // 2, SCREEN_H // 2 - 40)
        draw_text(screen, "Press ENTER to start — avoid campus hazards", 24, SCREEN_W // 2, SCREEN_H // 2 + 20)
        draw_text(screen, "Move with ← → or A D", 20, SCREEN_W // 2, SCREEN_H // 2 + 60)
        pygame.display.flip()
        clock.tick(FPS)


def level_loop(screen, clock, level_name):
    player = Player()
    obstacles = []
    spawn_timer = 0
    alive = True
    while True:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not alive and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False
        keys = pygame.key.get_pressed()
        if alive:
            player.update(keys)
            spawn_timer += dt
            if spawn_timer > 700:
                obstacles.append(Obstacle())
                spawn_timer = 0
            for ob in obstacles:
                ob.update()
            for ob in obstacles:
                if player.rect.colliderect(ob.rect):
                    alive = False
        screen.fill((230, 230, 230))
        draw_text(screen, f"Level: {level_name}", 26, SCREEN_W // 2, 30)
        player.draw(screen)
        for ob in obstacles:
            ob.draw(screen)
        if not alive:
            draw_text(screen, "You died! Press R to retry or Q to quit", 28, SCREEN_W // 2, SCREEN_H // 2)
        pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_caption("Waterloo Ways To Die")
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    title_screen(screen, clock)
    levels = [
        "Cycling on Ring Road (watch for buses)",
        "Crossing near SLC during icy weather",
        "Distracted walking — fountain zone",
    ]
    for level in levels:
        cont = level_loop(screen, clock, level)
        if not cont:
            break
    pygame.quit()


if __name__ == "__main__":
    main()
