OK_FORMAT = True

test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> set(faithful_residuals.labels) == set(['duration', 'wait', 'predicted wait', 'residual']) # Make sure your column labels are correct.\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> abs(sum(faithful_residuals.column('residual'))) <= 1e-8\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}