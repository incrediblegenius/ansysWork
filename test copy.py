#%%
from qd.cae.dyna import *

kf = KeyFile("AA.k", 
                 read_keywords=True, 
                 parse_mesh=True, 
                 load_includes=True)

kf.keys()
Keyword.field_alignment = Keyword.align.right
Keyword.name_alignment = Keyword.align.right

# %%
kw = kf['*KEYWORD'][0]
print(kw)
kw[0,0]=30000000
kw.reformat_all()
print(kw)
# %%
part_keywords = kf['*MAT_JOHNSON_COOK']

print(part_keywords)

# %%
print(part_keywords[0])
print(part_keywords[1])
print(part_keywords[2])
print(part_keywords[3])

# %%
kw = part_keywords[0]
kw[0,1] = 7.83
kw[0,2] = 0.77
kw[0,3] = 0.3
kw[1,0] = 7.92E-3
kw[1,1] = 5.1E-3
kw[1,2] = 0.26
kw[1,3] = 0.014
kw[1,4] = 1.03
kw[1,5] = 1793
kw[1,6] = 294
kw[1,7] = 0.1E-5
kw[2,0] = 0.477E-5
kw[2,1] = -9
kw[2,2] = 3
kw[2,4] = 0.8

kw.reformat_all()
print(kw)

#%%
kw = part_keywords[1]
kw[0,1] = 2.51
kw[0,2] = 7.77
kw[0,3] = 0.27
kw[1,0] = 7.92E-3
kw[1,1] = 5.1E-3
kw[1,2] = 0.26
kw[1,3] = 0.014
kw[1,4] = 1.03
kw[1,5] = 1793
kw[1,6] = 294
kw[1,7] = 0.1E-5
kw[2,0] = 0.477E-5
kw[2,1] = -9
kw[2,2] = 3
kw[2,4] = 0.8

kw.reformat_all()
print(kw)

#%%
kw = part_keywords[2]
kw[0,1] = 7.83
kw[0,2] = 0.77
kw[0,3] = 0.3
kw[1,0] = 7.92E-3
kw[1,1] = 5.1E-3
kw[1,2] = 0.26
kw[1,3] = 0.014
kw[1,4] = 1.03
kw[1,5] = 1793
kw[1,6] = 294
kw[1,7] = 0.1E-5
kw[2,0] = 0.477E-5
kw[2,1] = -9
kw[2,2] = 3
kw[2,4] = 0.8

kw.reformat_all()
print(kw)
#%%
kw = part_keywords[3]
kw[0,1] = 7.83
kw[0,2] = 0.77
kw[0,3] = 0.3
kw[1,0] = 7.92E-3
kw[1,1] = 5.1E-3
kw[1,2] = 0.26
kw[1,3] = 0.014
kw[1,4] = 1.03
kw[1,5] = 1793
kw[1,6] = 294
kw[1,7] = 0.1E-5
kw[2,0] = 0.477E-5
kw[2,1] = -9
kw[2,2] = 3
kw[2,4] = 0.8

kw.reformat_all()
print(kw)


# %%
print(part_keywords[0])
print(part_keywords[1])
print(part_keywords[2])
print(part_keywords[3])

# %%
part_keywords = kf['*EOS_GRUNEISEN']
for i in range(3):
    kw = part_keywords[i]
    kw[0,1] = 0.4569
    kw[0,2] = 1.49
    kw[0,3] = kw[0,4] = 0
    kw[0,5] = 2.17
    kw[0,6] = 0.46
    kw[0,7] = 0.00
    kw[1,0] = 1.0
    kw.reformat_all()
    print(kw)




# %%
part_keywords = kf['*BOUNDARY_SPC_SET']

# %%
kw = part_keywords[0]
kw[0,1] = kw[0,2] = kw[0,3] = kw[0,7] = 0
kw[0,4] = kw[0,5] = kw[0,6] = 1 
kw.reformat_all()
print(kw)
kw = part_keywords[1]
kw[0,1] = kw[0,3] = kw[0,4] = kw[0,5] = 0
kw[0,2] = kw[0,6] = kw[0,7] = 1 
kw.reformat_all()
print(kw)
kw = part_keywords[2]
kw[0,1] = kw[0,3] = 0
kw[0,4] = kw[0,2] = kw[0,5] = kw[0,6] = kw[0,7] = 1 
kw.reformat_all()
print(kw)


# %%
part_keywords = kf['*CONTACT_ERODING_SURFACE_TO_SURFACE']
for i in range(5):    
    print(part_keywords[i])
#%%
for i in range(6):
    kw = part_keywords[i]
    kw[1,4] = 0
    kw[1,5] = 0
    kw[1,6] = 0
    kw[1,7] = 0
    kw[3,0] = 1
    kw[3,1] = 1
    kw[3,2] = 1
    kw.reformat_all()
    print(kw)

# %%
part_keywords = kf['*CONTROL_TERMINATION']

kw = part_keywords[0]
print(kw)
kw[0,0] = 60
kw.reformat_all()
print(kw)

# %%
part_keywords = kf['*CONTROL_SHELL']
if len(part_keywords):
    kf.remove_keyword("*CONTROL_SHELL")
# # %%
# part_keywords = kf['*CONTROL_SHELL']
# print(part_keywords)

# %%
part_keywords = kf['*CONTROL_CONTACT']
kw = part_keywords[0]
print(kw)
kw[0,1]=kw[0,2]=kw[0,3]=kw[0,4]=kw[0,5]=kw[0,6] = 0
kw[1,1]=kw[1,2]=kw[1,3]=kw[1,4] = 0
kw.reformat_all()
print(kw)
# %%
part_keywords = kf['*INITIAL_VELOCITY_GENERATION']
kw = part_keywords[0]
print(kw)
kw[0,0] =1
kw[0,1] =2
kw[0,2] = kw[0,3] =0
kw[0,4] =-0.13
kw[1,0] = kw[1,1] = kw[1,2] = kw[1,3] =kw[1,4] = kw[1,5] =kw[1,6] = 0

kw.reformat_all()
print(kw)

# %%

kf.save(str(kf.get_filepath()))

# # %%
# from qd.cae.dyna import *
# import numpy as np
# d3plot = D3plot("../test3/d3plot", read_states=["vel","mises_stress max","strain inner"])
# part1 = d3plot.get_partByID(1)
# part2 = d3plot.get_partByID(2)
# ids1 = part1.get_node_ids()
# ids2 = part2.get_node_ids()
# # d3plot.get_element_energy(Element.solid)

# print("ids1[12] ="+str(ids1[12])+"\n")
# print(ids1[-1])

# print("ids2[12] ="+str(ids2[12]))


# # %%
# part.get_nNodes()

# # %%


# %%
