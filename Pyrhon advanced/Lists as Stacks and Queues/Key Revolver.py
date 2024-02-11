from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

used_bullets = 0
price_of_used_bullets = 0

while bullets and locks:
    current_bullets = bullets.pop()
    current_locks = locks.popleft()

    if current_bullets <= current_locks:
        used_bullets += 1
        price_of_used_bullets += bullet_price
        print("Bang!")
    else:
        locks.appendleft(current_locks)
        used_bullets += 1
        price_of_used_bullets += bullet_price
        print("Ping!")

    if used_bullets == gun_barrel_size:
        used_bullets = 0
        print("Reloading!")


locks_left = len(locks)

if locks_left == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - price_of_used_bullets}")
else:
    print(f"Couldn't get through. Locks left: {locks_left}")