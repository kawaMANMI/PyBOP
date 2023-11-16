from scipy.optimize import minimize
from .base_optimiser import BaseOptimiser


class SciPyMinimize(BaseOptimiser):
    """
    Wrapper class for the SciPy optimisation class. Extends the BaseOptimiser class.
    """

    def __init__(self, method=None, bounds=None):
        super().__init__()
        self.name = "SciPyMinimize"
        self.method = method
        self.bounds = bounds

        if self.method is None:
            self.method = "L-BFGS-B"

    def _runoptimise(self, cost_function, x0, bounds):
        """
        Run the SciPy optimisation method.

        Inputs
        ----------
        cost_function: function for optimising
        method: optimisation algorithm
        x0: initialisation array
        bounds: bounds array
        """

        if bounds is not None:
            # Reformat bounds and run the optimser
            bounds = (
                (lower, upper) for lower, upper in zip(bounds["lower"], bounds["upper"])
            )
            output = minimize(cost_function, x0, method=self.method, bounds=bounds)
        else:
            output = minimize(cost_function, x0, method=self.method)

        # Get performance statistics
        x = output.x
        final_cost = output.fun

        return x, final_cost

    def needs_sensitivities(self):
        """
        Returns True if the optimiser needs sensitivities.
        """
        return False
