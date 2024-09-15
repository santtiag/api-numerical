
class URL:
    def __init__(self, home_t):
        self.home_t = home_t 
        self.home = self.Home(home_t)

    class Home:
        def __init__(self, home_t, inter_t = '/interpolation', reg_t = '/regression'):
            self.inter = self.Interpolation(f'{home_t}{inter_t}')
            self.reg = self.Regression(f'{home_t}{reg_t}')

        class Interpolation:
            def __init__(self, inter_t):
                self.lin_seg = f"{inter_t}/linear_segmentation"
                self.quad_seg = f"{inter_t}/quadratic_segmentation"
                self.cub_seg = f"{inter_t}/cubic_segmentation"

        class Regression:
            def __init__(self, reg_t, nonlin_t = '/nonlinear'):
                self.lin = f"{reg_t}/linear"
                self.nonlin = self.NonLinear(f'{reg_t}{nonlin_t}')

            class NonLinear:
                def __init__(self, nonlin_t):
                    self.exp = f"{nonlin_t}/exponential"
                    self.pot = f"{nonlin_t}/potential"
                    self.poly = f"{nonlin_t}/polynomial"

