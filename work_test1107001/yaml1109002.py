import yaml
with open("test1109002.yaml","r") as file:
    confile=yaml.safe_load(file)
print(confile)



work1 =  [{"sid": "001", "name": "guanyuchang", "age": "17", "gender": "M"}, {"sid": "003", "name": "sunshangxaing", "age": 22, "gender": "W"}, {"sid": "002", "name": "sunquan", "age": 34, "gender": "M"}, {"sid": "004", "name": "zhangfei", "age": 43, "gender": "M"}, {"sid": "005", "name": "sunquan", "age": 23, "gender": "W"}, {"sid": "009", "name": "hanc", "age": "21", "gender": "M"}, {"sid": "008", "name": "zhaofei", "age": "18", "gender": "W"}, {"sid": "007", "name": "eqw", "age": "12", "gender": "W"}]

with open("test1109002.yaml","w") as file:
    confile = yaml.safe_dump(work1,file)