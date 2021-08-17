# https://www.acmicpc.net/problem/3190

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
K_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
L_lst = [sys.stdin.readline().strip() for _ in range(L)]

seconds = 0
is_dead = False
game_time = 0

snake_que = [[1, 1]]
snake_length = 1
snake_head_index = 0
snake_heading = 'R' #'L', 'U', 'D'

for info in L_lst:
    move = info.split() # 3, D
    times = int(move[0]) - seconds

    if snake_heading == 'R':
        for _ in range(times): #3초 동안
            seconds += 1
            next_move = [snake_que[snake_head_index][0], snake_que[snake_head_index][1]+1]
            
            if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
                is_dead = True
                game_time = seconds
            
            for i in range(snake_head_index, snake_head_index-snake_length, -1):
                if next_move == snake_que[i]:
                    is_dead = True
                    game_time = seconds

            if is_dead:
                break

            snake_que.append(next_move)
            snake_head_index += 1

            if snake_que[snake_head_index] in K_lst:
                K_lst.remove(snake_que[snake_head_index])
                snake_length += 1

        if is_dead:
            break
        elif move[1] == 'L':
            snake_heading = 'U'
        elif move[1] == 'D':
            snake_heading = 'D'
    elif snake_heading == 'L':
        for _ in range(times): #3초 동안
            seconds += 1
            next_move = [snake_que[snake_head_index][0], snake_que[snake_head_index][1]-1]

            if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
                is_dead = True
                game_time = seconds
            
            for i in range(snake_head_index, snake_head_index-snake_length, -1):
                if next_move == snake_que[i]:
                    is_dead = True
                    game_time = seconds
            
            if is_dead:
                break

            snake_que.append(next_move)
            snake_head_index += 1

            if snake_que[snake_head_index] in K_lst:
                K_lst.remove(snake_que[snake_head_index])
                snake_length += 1

        if is_dead:
            break
        elif move[1] == 'L':
            snake_heading = 'D'
        elif move[1] == 'D':
            snake_heading = 'U'
    elif snake_heading == 'D':

        for _ in range(times): #3초 동안
            seconds += 1
            next_move = [snake_que[snake_head_index][0]+1, snake_que[snake_head_index][1]]

            if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
                is_dead = True
                game_time = seconds

            for i in range(snake_head_index, snake_head_index-snake_length, -1):
                if next_move == snake_que[i]:
                    is_dead = True
                    game_time = seconds

            if is_dead:
                break

            snake_que.append(next_move)
            snake_head_index += 1

            if snake_que[snake_head_index] in K_lst:
                K_lst.remove(snake_que[snake_head_index])
                snake_length += 1

        if is_dead:
            break  
        elif move[1] == 'L':
            snake_heading = 'R'
        elif move[1] == 'D':
            snake_heading = 'L'
    elif snake_heading == 'U':
        for _ in range(times): #3초 동안
            seconds += 1
            next_move = [snake_que[snake_head_index][0]-1, snake_que[snake_head_index][1]]

            if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
                is_dead = True
                game_time = seconds
            
            for i in range(snake_head_index, snake_head_index-snake_length, -1):
                if next_move == snake_que[i]:
                    is_dead = True
                    game_time = seconds

            if is_dead:
                break

            snake_que.append(next_move)
            snake_head_index += 1

            if snake_que[snake_head_index] in K_lst:
                K_lst.remove(snake_que[snake_head_index])
                snake_length += 1

        if is_dead:
            break   
        elif move[1] == 'L':
            snake_heading = 'L'
        elif move[1] == 'D':
            snake_heading = 'R'

    if is_dead:
        break

while is_dead == False:
    if snake_heading == 'R':
        seconds += 1
        next_move = [snake_que[snake_head_index][0], snake_que[snake_head_index][1]+1]

        if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
            is_dead = True
            game_time = seconds

        for i in range(snake_head_index, snake_head_index-snake_length, -1):
            if next_move == snake_que[i]:
                is_dead = True
                game_time = seconds

        snake_que.append(next_move)
        snake_head_index += 1

        if snake_que[snake_head_index] in K_lst:
            K_lst.remove(snake_que[snake_head_index])
            snake_length += 1
    elif snake_heading == 'L':
        seconds += 1
        next_move = [snake_que[snake_head_index][0], snake_que[snake_head_index][1]-1]

        if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
            is_dead = True
            game_time = seconds

        for i in range(snake_head_index, snake_head_index-snake_length, -1):
            if next_move == snake_que[i]:
                is_dead = True
                game_time = seconds

        snake_que.append(next_move)
        snake_head_index += 1

        if snake_que[snake_head_index] in K_lst:
            K_lst.remove(snake_que[snake_head_index])
            snake_length += 1
    elif snake_heading == 'D':
        seconds += 1
        next_move = [snake_que[snake_head_index][0]+1, snake_que[snake_head_index][1]]

        if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
            is_dead = True
            game_time = seconds

        for i in range(snake_head_index, snake_head_index-snake_length, -1):
            if next_move == snake_que[i]:
                is_dead = True
                game_time = seconds

        snake_que.append(next_move)
        snake_head_index += 1

        if snake_que[snake_head_index] in K_lst:
            K_lst.remove(snake_que[snake_head_index])
            snake_length += 1
    elif snake_heading == 'U':
        seconds += 1
        next_move = [snake_que[snake_head_index][0]-1, snake_que[snake_head_index][1]]

        if next_move[0] > N or next_move[0] < 1 or next_move[1] > N or next_move[1] < 1:
            is_dead = True
            game_time = seconds

        for i in range(snake_head_index, snake_head_index-snake_length, -1):
            if next_move == snake_que[i]:
                is_dead = True
                game_time = seconds

        snake_que.append(next_move)
        snake_head_index += 1

        if snake_que[snake_head_index] in K_lst:
            K_lst.remove(snake_que[snake_head_index])
            snake_length += 1

print(game_time)