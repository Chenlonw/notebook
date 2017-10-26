import timeit

cy = timeit.timeit('example_cy.test(5)', setup='import example_cy', number=100)
py = timeit.timeit('example_py.test(5)', setup='import example_py', number=100)

print 'Cython is {}x faster'.format(py/cy)
