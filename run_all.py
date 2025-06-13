from simulate_mode import simulate_mode
from puzzles.hanoi import sample as hanoi_sample, grade as hanoi_grade
from puzzles.checkers import sample as checkers_sample, grade as checkers_grade
from puzzles.river import sample as river_sample, grade as river_grade
from puzzles.blocks import sample as blocks_sample, grade as blocks_grade

simulate_mode("Hanoi", lambda: hanoi_sample(25), hanoi_grade, "hanoi", rounds=25)
simulate_mode("Checkers", lambda: checkers_sample(25), checkers_grade, "checkers", rounds=25)
simulate_mode("River", lambda: river_sample(25), river_grade, "river", rounds=25)
simulate_mode("Blocks", lambda: blocks_sample(25), blocks_grade, "blocks", rounds=25)
