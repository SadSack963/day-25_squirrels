import pandas

"""
Program to collate NYC squirrel data.
    tabulate fur colour and totals
"""

data_frame = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# colors = data_frame["Primary Fur Color"].unique()
# print("\ncolors\n", colors)
# # [nan 'Gray' 'Cinnamon' 'Black'], nan = No color specified
#
# group = data_frame.groupby(["Primary Fur Color"], dropna=False)
# print("\ngroup\n", group)
# # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A943D6A5E0>
# print("\ntype(group)\n", type(group))
# # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
# print("\ngroup.size()\n", group.size())
# # Primary Fur Color
# # Black        103
# # Cinnamon     392
# # Gray        2473
# # NaN           55
# # dtype: int64
#
# # count = data_frame.groupby(["Primary Fur Color"], dropna=False).size().reset_index(name='Count')
# # print("\ncount\n", count)
# #   Primary Fur Color  Count
# # 0             Black    103
# # 1          Cinnamon    392
# # 2              Gray   2473
# # 3               NaN     55

count = data_frame.groupby(["Primary Fur Color"]).size().reset_index(name='Count')
# print("\ncount\n", count)
#   Primary Fur Color  Count
# 0             Black    103
# 1          Cinnamon    392
# 2              Gray   2473


count.to_csv("color_count.csv")
