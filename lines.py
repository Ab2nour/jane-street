from square_logic import LineLogic


def line_8_zones(line_logic: LineLogic):
    line = line_logic
    line.add_link(0,1)
    line.diff_link(1,2)
    line.diff_link(2,3)
    line.diff_link(3,4)
    line.diff_link(4,5)
    line.add_link(5,6)
    line.diff_link(6,7)
    line.add_link(7,8)
    line.diff_link(8,9)
    line.diff_link(9,10)