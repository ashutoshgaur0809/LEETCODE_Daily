a = ["d1/","d2/","../","d21/","./"]


st = []
for i in a:
    if i != "../":
        if i != "./":
            st.append(i)
    if i == "../":
        st.pop()


print(st)
