df0 = pd.read_csv("../input/covidglobal/CONVENIENT_global_confirmed_cases.csv")
df1 = pd.read_csv("../input/covidglobal/CONVENIENT_global_deaths.csv")
#Data Preparation
world = pd.DataFrame({"Country":[],"Cases":[]})
world["Country"] = df0.iloc[:,1:].columns
cases = []
for i in world["Country"]:
    cases.append(pd.to_numeric(df0[i][1:]).sum())
world["Cases"]=cases

country_list=list(world["Country"].values)
idx = 0
for i in country_list:
    sayac = 0
    for j in i:
        if j==".":
            i = i[:sayac]
            country_list[idx]=i
        elif j=="(":
            i = i[:sayac-1]
            country_list[idx]=i
        else:
            sayac += 1
    idx += 1
world["Country"]=country_list
world = world.groupby("Country")["Cases"].sum().reset_index()
world.head()
continent=pd.read_csv("../input/covidglobal/continents2.csv")
continent["name"]=continent["name"].str.upper()
