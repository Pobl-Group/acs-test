import pandas as pd

d = {}
d["col_a"] = ["a", "b", "c"]
d["col_b"] = [1, 2, 3]
d["col_c"] = [True, False, None]
df = pd.DataFrame.from_dict(d)
print(df)
