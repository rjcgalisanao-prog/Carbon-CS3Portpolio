import random
import time
import turtle


WIDTH, HEIGHT = 800, 600
LEFT, RIGHT = -380, 380
BOTTOM, TOP = -270, 220


class Ship:
    name = "Ship"
    max_hull = 100
    speed = 5
    skill_name = "Special skill"

    def __init__(self):
        self.hull = self.max_hull
        self.turtle = turtle.Turtle()
        self.turtle.shape("triangle")
        self.turtle.color("cyan")
        self.turtle.shapesize(1.4)
        self.turtle.setheading(90)
        self.turtle.penup()

    def activate_skill(self, game, now):
        raise NotImplementedError


class Fighter(Ship):
    name = "Fighter"
    max_hull = 100
    speed = 5
    skill_name = "Shield"

    def activate_skill(self, game, now):
        game.shield_until = now + 3
        game.message = "Fighter shield: damage blocked for 3 seconds!"


class Scout(Ship):
    name = "Scout"
    max_hull = 75
    speed = 6
    skill_name = "Speed boost"

    def activate_skill(self, game, now):
        game.speed_until = now + 3
        game.message = "Scout boost: faster movement for 3 seconds!"


class Bomber(Ship):
    name = "Bomber"
    max_hull = 130
    speed = 4
    skill_name = "Shockwave"

    def activate_skill(self, game, now):
        destroyed = 0
        x, y = self.turtle.position()

        for meteor in game.meteors:
            close_x = abs(meteor.turtle.xcor() - x) < 150
            close_y = abs(meteor.turtle.ycor() - y) < 150
            if not meteor.destroyed and close_x and close_y:
                meteor.destroyed = True
                destroyed += 1

        game.message = f"Bomber shockwave destroyed {destroyed} meteor(s)!"


class Medic(Ship):
    name = "Medic"
    max_hull = 90
    speed = 5
    skill_name = "Repair"

    def activate_skill(self, game, now):
        self.hull = min(self.max_hull, self.hull + 30)
        game.message = "Medic repair: restored up to 30 hull!"


class CargoShip(Ship):
    name = "Cargo Ship"
    max_hull = 150
    speed = 3.5
    skill_name = "Supply barrier"

    def activate_skill(self, game, now):
        game.barrier_until = now + 4
        game.message = "Supply barrier: meteors won't hurt you for 4 seconds!"


class Meteor:
    def __init__(self, x, y, score):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(random.choice(["gray", "sienna", "dim gray"]))
        self.turtle.shapesize(random.uniform(0.8, 1.4))
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.destroyed = False

        difficulty = score // 5
        slow_speed = min(1.5 + difficulty * 0.15, 6.5)
        fast_speed = min(2.8 + difficulty * 0.20, 9.0)
        self.speed = random.uniform(slow_speed, fast_speed)

    def move(self):
        self.turtle.sety(self.turtle.ycor() - self.speed)


class Bullet:
    def __init__(self, x, y):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("yellow")
        self.turtle.shapesize(0.35)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.destroyed = False

    def move(self):
        self.turtle.sety(self.turtle.ycor() + 9)


class SpaceGame:
    ship_types = [Fighter, Scout, Bomber, Medic, CargoShip]

    def __init__(self, screen):
        self.screen = screen
        self.keys_down = set()
        self.meteors = []
        self.bullets = []
        self.score = 0
        self.last_shot = 0
        self.last_meteor = 0
        self.last_skill = 0
        self.skill_cooldown = 5
        self.shield_until = 0
        self.speed_until = 0
        self.barrier_until = 0
        self.message = "Destroy meteors and stay alive!"
        self.game_over = False

        self.ship = Fighter()

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)

        self.hud = turtle.Turtle()
        self.hud.hideturtle()
        self.hud.penup()
        self.hud.speed(0)

        self.bind_controls()
        self.draw_button()
        self.update()

    def bind_controls(self):
        for key in ("w", "a", "s", "d", "space"):
            self.screen.onkeypress(
                lambda k=key: self.keys_down.add(k), key
            )
            self.screen.onkeyrelease(
                lambda k=key: self.keys_down.discard(k), key
            )

        self.screen.onkeypress(self.use_skill, "e")

        for number in range(1, 6):
            self.screen.onkeypress(
                lambda n=number: self.switch_ship(n - 1),
                str(number),
            )

        self.screen.onclick(self.handle_click)
        self.screen.listen()

    def draw_button(self):
        self.pen.clear()
        self.pen.goto(275, -265)
        self.pen.color("white")
        self.pen.write(
            "[ FIRE ]",
            align="center",
            font=("Arial", 16, "bold"),
        )

    def handle_click(self, x, y):
        if 230 < x < 370 and -285 < y < -235:
            self.shoot()

    def switch_ship(self, index):
        if self.game_over:
            return

        hull_fraction = self.ship.hull / self.ship.max_hull
        old_x, old_y = self.ship.turtle.position()
        self.ship.turtle.hideturtle()

        self.ship = self.ship_types[index]()
        self.ship.hull = max(1, int(self.ship.max_hull * hull_fraction))
        self.ship.turtle.goto(old_x, old_y)
        self.message = f"Switched to {self.ship.name}!"

    def shoot(self):
        now = time.monotonic()

        if not self.game_over and now - self.last_shot >= 0.25:
            x, y = self.ship.turtle.position()
            self.bullets.append(Bullet(x, y + 15))
            self.last_shot = now

    def use_skill(self):
        now = time.monotonic()

        if not self.game_over and now - self.last_skill >= self.skill_cooldown:
            self.ship.activate_skill(self, now)
            self.last_skill = now

    def move_player(self, now):
        player = self.ship.turtle
        move_x = 0
        move_y = 0

        if "a" in self.keys_down:
            move_x -= 1
        if "d" in self.keys_down:
            move_x += 1
        if "w" in self.keys_down:
            move_y += 1
        if "s" in self.keys_down:
            move_y -= 1

        speed = self.ship.speed
        if now < self.speed_until:
            speed *= 1.7

        new_x = player.xcor() + move_x * speed
        new_y = player.ycor() + move_y * speed

        player.goto(
            max(LEFT, min(RIGHT, new_x)),
            max(BOTTOM, min(TOP, new_y)),
        )

    def update_meteors(self, now):
        # Spawn interval gets shorter as the score increases.
        spawn_interval = max(0.18, 0.8 - self.score * 0.008)

        if now - self.last_meteor > spawn_interval:
            self.meteors.append(
                Meteor(random.randint(LEFT, RIGHT), TOP + 50, self.score)
            )
            self.last_meteor = now

        player_x = self.ship.turtle.xcor()
        player_y = self.ship.turtle.ycor()

        for meteor in self.meteors:
            if meteor.destroyed:
                continue

            meteor.move()

            close_x = abs(meteor.turtle.xcor() - player_x) < 22
            close_y = abs(meteor.turtle.ycor() - player_y) < 22

            if close_x and close_y:
                meteor.destroyed = True

                if now >= self.shield_until and now >= self.barrier_until:
                    self.ship.hull = max(0, self.ship.hull - 15)
                    self.message = "Meteor hit! You lost 15 hull."
                else:
                    self.message = "Your defense blocked a meteor!"

            if meteor.turtle.ycor() < BOTTOM - 40:
                meteor.destroyed = True

        self.meteors = self.remove_destroyed(self.meteors)

    def update_bullets(self):
        for bullet in self.bullets:
            if bullet.destroyed:
                continue

            bullet.move()

            if bullet.turtle.ycor() > TOP + 50:
                bullet.destroyed = True
                continue

            for meteor in self.meteors:
                close_x = abs(
                    bullet.turtle.xcor() - meteor.turtle.xcor()
                ) < 20
                close_y = abs(
                    bullet.turtle.ycor() - meteor.turtle.ycor()
                ) < 20

                if not meteor.destroyed and close_x and close_y:
                    meteor.destroyed = True
                    bullet.destroyed = True
                    self.score += 1
                    self.message = "Meteor destroyed!"
                    break

        self.bullets = self.remove_destroyed(self.bullets)
        self.meteors = self.remove_destroyed(self.meteors)

    @staticmethod
    def remove_destroyed(items):
        remaining = []

        for item in items:
            if item.destroyed:
                item.turtle.hideturtle()
            else:
                remaining.append(item)

        return remaining

    def draw_health_bar(self):
        x, y = -370, 260
        width, height = 220, 16
        fill_width = width * self.ship.hull / self.ship.max_hull

        self.hud.penup()
        self.hud.goto(x, y)
        self.hud.color("red")
        self.hud.begin_fill()
        self.hud.goto(x + width, y)
        self.hud.goto(x + width, y + height)
        self.hud.goto(x, y + height)
        self.hud.goto(x, y)
        self.hud.end_fill()

        self.hud.goto(x, y)
        self.hud.color("lime green" if self.ship.hull > 30 else "orange")
        self.hud.begin_fill()
        self.hud.goto(x + fill_width, y)
        self.hud.goto(x + fill_width, y + height)
        self.hud.goto(x, y + height)
        self.hud.goto(x, y)
        self.hud.end_fill()

    def draw_hud(self, now):
        self.hud.clear()
        self.draw_health_bar()

        self.hud.goto(-370, 282)
        self.hud.color("white")
        self.hud.write(
            f"{self.ship.name}  Hull: {self.ship.hull}/{self.ship.max_hull}",
            font=("Arial", 12, "normal"),
        )

        difficulty = self.score // 5 + 1
        skill_left = max(
            0,
            self.skill_cooldown - (now - self.last_skill),
        )
        skill_status = "READY" if skill_left == 0 else f"{skill_left:.1f}s"

        self.hud.goto(40, 270)
        self.hud.write(
            f"Score: {self.score}  Difficulty: {difficulty}  "
            f"Skill: E ({self.ship.skill_name}) {skill_status}",
            font=("Arial", 11, "normal"),
        )

        self.hud.goto(0, -295)
        self.hud.write(
            "WASD move | Space or click FIRE to shoot | 1-5 change ship | E skill",
            align="center",
            font=("Arial", 10, "normal"),
        )

        self.hud.goto(0, 235)
        self.hud.write(
            self.message,
            align="center",
            font=("Arial", 12, "normal"),
        )

        if now < self.shield_until:
            status = "SHIELD ACTIVE"
        elif now < self.barrier_until:
            status = "BARRIER ACTIVE"
        else:
            status = ""

        if status:
            self.hud.goto(0, 210)
            self.hud.write(status, align="center", font=("Arial", 12, "bold"))

    def update(self):
        if not self.game_over:
            now = time.monotonic()

            self.move_player(now)
            self.update_meteors(now)
            self.update_bullets()

            if "space" in self.keys_down:
                self.shoot()

            if self.ship.hull <= 0:
                self.game_over = True
                self.message = "ggs well played buseng mahina ka pa"
                self.ship.turtle.color("red")

            self.draw_hud(now)

        self.screen.update()
        self.screen.ontimer(self.update, 20)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Miss u bibi")
    screen.bgcolor("black")
    screen.tracer(0)

    SpaceGame(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()