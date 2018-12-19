global_var = 1
def my_vars():
    print ("Global variable:", global_var)
    local_var = 2
    print ("Local variable:", local_var)

my_vars()
try:
    print ("Local Variable called from outside of function is:", local_var)
except:
    print ("local_var is not available")
