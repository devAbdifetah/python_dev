def display_info(a,b,*args, instructor="colt", **kwargs):
     return (a,b,args, instructor, kwargs)
print(display_info(1,2,3,last_name="Hassan",job="webDev"))
