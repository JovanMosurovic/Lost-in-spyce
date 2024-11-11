import random


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
        my_stack = [(state, [])]
        visited = set()

        while my_stack:
            current_state, path = my_stack.pop()

            if current_state.is_goal_state():
                return path

            if current_state.get_state('S') not in visited:
                visited.add(current_state.get_state('S'))
                for action in reversed(current_state.get_legal_actions()):
                    next_state = current_state.generate_successor_state(action)
                    my_stack.append((next_state, path + [action]))
        return None

class Red(Algorithm):
    def get_path(self, state): # BFS
        my_queue = [(state, [])]
        visited = set()

        while my_queue:
            current_state, path = my_queue.pop()

            if current_state.is_goal_state():
                return path

            if current_state.get_state('S') not in visited:
                visited.add(current_state.get_state('S'))
                for action in current_state.get_legal_actions():
                    next_state = current_state.generate_successor_state(action)
                    my_queue.insert(0, (next_state, path + [action]))
        return None










