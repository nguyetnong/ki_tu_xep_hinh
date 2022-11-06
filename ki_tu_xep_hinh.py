
ki_tu = input('Your char?: ')
chieu_dai=int(input("chieu dai:"))
chieu_cao=int(input("chieu cao:"))

#print(int(ki_tu)*chieu_dai)
#print(ki_tu+" "+(chieu_dai-2)+ki_tu)

for i in range(chieu_cao):
    if i==0 or (i == chieu_cao-1):
        print(ki_tu*(chieu_dai))
    else:
        print(ki_tu+" "*((chieu_dai)-2) +" "+ki_tu)
        
   