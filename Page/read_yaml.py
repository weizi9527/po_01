
    arrs=[]
    for i in get_yaml1().values():
        aarrs.append((i.get("uesrname"),i.get("password"),i.get("expect_toast")))
    print(arrs)