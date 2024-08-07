class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(len(positions))])

        stack = [] 
        for position, health, direction, index in robots:
            if direction == 'R':
                stack.append((position, health, direction, index))
            else:  # direction == 'L'
                while stack and stack[-1][2] == 'R':
                    r_pos, r_health, r_direction, r_index = stack.pop()
                    if r_health > health:
                        stack.append((r_pos, r_health - 1, r_direction, r_index))
                        health = -1
                        break
                    elif r_health < health:
                        health -= 1
                    else:
                        health = -1
                        break
                if health != -1:
                    stack.append((position, health, direction, index))
        surviving_healths = [None] * len(positions)
        for _, health, _, index in stack:
            surviving_healths[index] = health
        return [h for h in surviving_healths if h is not None]