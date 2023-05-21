class Model:
    model_value = 0

    cmd_mult = 7.2
    mov_mult = 1.2
    skl_mult = 8
    def_mult = 9
    tgh_mult = 18
    hp_mult = 20

    game_div = 700

    def __init__(self, name, att_cmd, att_mov, att_skl, att_def, att_tgh, att_hp, special_rules = []):
        self.name = name
        self.att_cmd = att_cmd
        self.att_mov = att_mov
        self.att_skl = 6 - att_skl
        self.att_def = 6 - att_def
        self.att_tgh = att_tgh
        self.att_hp  = att_hp
        self.special_rules = special_rules
    
    def calculate_base_value(self):
        base_value = 0
        # print(self.name)
        base_value += Model.mov_mult * self.att_mov
        # print(Model.mov_mult * self.att_mov)
        base_value += Model.skl_mult * self.att_skl
        # print(Model.skl_mult * self.att_skl)
        base_value += Model.def_mult * self.att_def
        # print(Model.def_mult * self.att_def)
        base_value += Model.tgh_mult * self.att_tgh
        # print(Model.tgh_mult * self.att_tgh)
        base_value += Model.hp_mult * self.att_hp
        # print(Model.hp_mult * self.att_hp)
        base_value += (Model.cmd_mult * base_value) * self.att_cmd
        # print(base_value / Model.game_div)
        print(self.name + ": " + str(round(base_value / Model.game_div)))

new_model = Model("Wych",4,8,4,6,2,3)
new_model.calculate_base_value()

new_model2 = Model("Warrior",4,6,4,5,2,3)
new_model2.calculate_base_value()

better_model = Model("Space Marine",5,6,3,3,4,4)
better_model.calculate_base_value()

better_model2 = Model("BigMan", 6,6,2,2,5,5)
better_model2.calculate_base_value()