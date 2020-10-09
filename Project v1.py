map = [['e','e','e','P<','e','e','e','e','e'],##Inglenook layout using the 'P' to designate
       ['P<','e','e','e'],## a point and the arrow to do the direction.
       ['e','e','e']]

points=[{3:[0,[1,0]]},## points position in the original row
        {0:[0,[2,0]]}]

def point_changer(points,point_num):
    if points[point_num][0]=0:
        points[point_num][0]=1
    else:
        points[point_num][0]=0
    return points

def move(map,direction,row_num,berth_num,points):
    if berth_num>0 and berth_num<(len(map[row_num])-1):
        berth_num=berth_num+direction
    if map[row_num][berth_num][0]=='P' and points[row_num][berth_num][0]==1:
        if map[row_num][berth_num][1]=='<' and direction>0:
            row_num=points[row_num][berth_num][1][0]
            berth_num=points[row_num][berth_num][1][1]
        elif map[row_num][berth_num][1]=='<' and direction>0:
            row_num=points[row_num][berth_num][1][0]
            berth_num=points[row_num][berth_num][1][1]
    return row_num,berth_num