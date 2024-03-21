class Mux4:
    """(B,A) -> ch"""
    def __init__(self, sel_a, sel_b) -> None:
        self.sel_a = sel_a 
        self.sel_b = sel_b

    def select(self, ch_num: int):
        """ch_num = 0 ~ 3"""
        self.sel_b.on() if ch_num // 2 else self.sel_b.off()
        self.sel_a.on() if ch_num % 2 else self.sel_a.off()
                                                                                                                                
class Mux16(Mux4):
    def select(self, ch_num: int):
        """ch_num = 0 ~ 15"""
        self.sel_b.on() if ch_num // 8 else self.sel_b.off()
        self.sel_a.on() if ch_num // 4 % 2 else self.sel_a.off()