'''
From match.csv, creating matchreport.csv by calculating matchplayed and points gained by each team using python
'''
f=open("match.csv","r")
f1=open("matchreport.csv","w")
next(f)
f1.write("Team,Match_Played,Wins,Draw,Loss,Points")
for x in f:
    to=x.split(",")
    print(to)
    team=to[0]
    win=to[1]
    draw=to[2]
    loss=int(to[3])
    points=int(win)*3+int(draw)*1
    matchplayed=int(win)+int(draw)+int(loss)
    f1.write(f"\n{team},{matchplayed},{win},{draw},{loss},{points}")




    
