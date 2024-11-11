import random

from pygame.mixer_music import queue


class Algorithm:
    def get_path(self, state):
        pass


class ExampleAlgorithm(Algorithm):
    def get_path(self, state):
        path = []
        while not state.is_goal_state():
            possible_actions = state.get_legal_actions()
            action = possible_actions[random.randint(0, len(possible_actions) - 1)]
            path.append(action)
            state = state.generate_successor_state(action)
        return path

class Blue(Algorithm):
    def get_path(self, state): # DFS
        stack = [(state, [])]
        visited = set()

        while stack:
            current_state, path = stack.pop()

            if current_state.is_goal_state():
                return path

            if current_state.get_state('S') not in visited:
                visited.add(current_state.get_state('S'))
                for action in reversed(current_state.get_legal_actions()):
                    next_state = current_state.generate_successor_state(action)
                    stack.append((next_state, path + [action]))
        return None






