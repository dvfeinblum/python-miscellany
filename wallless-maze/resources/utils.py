class GameState:
    def __init__(self, move_count=0, move_list='', current_pos=tuple(), starting_pos=tuple()):
        self.move_count = move_count
        self.move_list = move_list
        self.current_pos = current_pos
        self.starting_pos = starting_pos

    def clone_state(self, current_pos=None, move=None):
        if current_pos and move:
            return GameState(move_count=self.move_count,
                             move_list=self.move_list[:-1] + move,
                             current_pos=current_pos,
                             starting_pos=self.starting_pos)
        else:
            return GameState(move_count=self.move_count,
                             move_list=self.move_list,
                             current_pos=self.current_pos,
                             starting_pos=self.starting_pos)

    def __str__(self):
        return ('Move Count: {cnt}\n'
                'Move List: {lst}\n'
                'Starting Position: {strt}\n').format(cnt=self.move_count,
                                                      lst=self.move_list,
                                                      strt=self.starting_pos)
