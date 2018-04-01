from desc import description

def function(x=[], a1=1, a2=1, a3=1, a4=1):
    print description.description()
    result = a1 * x[0]**3;
    result += a2 * x[1]**2;
    result += a3 * x[2];
    result += a4;
    return result;

if __name__ == '__main__':
    variable = [1,2,3]
    print function(x = variable)
    
    
