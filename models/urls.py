class URL:
    def __init__(self, home_t):
        self.home_t = home_t
        self.home = self.Home(home_t)

    class Home:
        def __init__(
            self, home_t,
            inter_t = '/interpolation',
            reg_t = '/regression',
            d_i_t='/definite_integration',
            meth_t='/methodology',
            d_e_t='/differential_equation'
        ):
            self.inter = self.Interpolation(f'{home_t}{inter_t}')
            self.reg = self.Regression(f'{home_t}{reg_t}')
            self.d_i = self.DefiniteIntegration(f'{home_t}{d_i_t}')
            self.meth = self.Methodology(f'{home_t}{meth_t}')
            self.d_e = self.Differential_Equation(f'{home_t}{d_e_t}')

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

        class DefiniteIntegration:
            def __init__(self, d_i_t):
                self.rect = f"{d_i_t}/rectangle"
                self.trap = f"{d_i_t}/trapezium"
                self.para = f"{d_i_t}/parabola"
                self.ca = f"{d_i_t}/cubic_approximation"
        class Methodology:
            def __init__(self, meth_t):
                self.gauss = f"{meth_t}/gauss"
                self.boole = f"{meth_t}/boole"

        class Differential_Equation:
            def __init__(self, d_e_t):
                self.lin_approx = f"{d_e_t}/linear_approximation"
                self.quad_approx = f"{d_e_t}/quadratic_approximation"
                self.grade_4_approx = f"{d_e_t}/grade_4_approximation"
