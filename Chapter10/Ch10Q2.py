st = input('Enter no one by one separated by space:')
st = st.split()
#n = list(st)
n = [eval(x) for x in st]
n.reverse()
print(n)
