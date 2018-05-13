import numpy
def run_real_model_inner(p, input_Xi):
    shape_v = input_Xi.shape
    l = [1, 5, 9]
    s = 0
    sa = 0
    for i in range(shape_v[1]):
        s = s+l[i]*input_Xi[0, i]**(i+1)
        sa = sa+l[i]*input_Xi[0, i]**(i+4)

    shape_va = p.shape
    ts = 0
    for i in range(shape_va[1]):
        ts = ts+p[0, i]

    ts = ts**2
    s = s+ts
    ts = ts**4
    sa = sa+ts
    return s, sa

def run_real_model(p, input_X):
    shape_v = input_X.shape
    ret = run_real_model_inner(p[0], input_X[0])
    for i in range(shape_v[0]):
        if i == 0:
            continue
        tret = run_real_model_inner(p[0], input_X[i])
        ret = numpy.row_stack((ret, tret))

    shape_v1 = p.shape
    ret = numpy.mat(ret)

    for i in range(shape_v1[0]):
        if i == 0:
            continue
        shape_v = input_X.shape
        ret_a = run_real_model_inner(p[i], input_X[0])
        for ia in range(shape_v[0]):
            if ia == 0:
                continue
            tret = run_real_model_inner(p[i], input_X[ia])
            ret_a = numpy.row_stack((ret_a, tret))
        ret_a = numpy.mat(ret_a)
        ret = ret+ret_a

    ret = ret/shape_v1[0]
    return ret
