import pandas as pd
import xml.etree.ElementTree as et

xtree = et.parse("14_04.xml")
xroot = xtree.getroot()

df_cols =["id" , "createAt" , "name" , "age"]
rows = []

for node in xroot:
    s_id = node.attrib.get("id")
    s_createAt = node.attrib.get("createAt")
    s_name = node.find("name").text if node is  not None else None
    s_age = node.find("age").text if node is  not None else None

    rows.append({"id":s_id , "createAt":s_createAt, "name":s_name, "age":s_age })

out_df = pd.DataFrame(rows , columns = df_cols)