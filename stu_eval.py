import sys
if len(sys.argv) == 6:
  s1 = sys.argv[1]
  s2 = sys.argv[2]
  s3 = sys.argv[3]
  s4 = sys.argv[4]
  s5 = sys.argv[5]
  avg = (s1+s2+s3+s4+s5)/5
  print("Average marks: ", avg)

else:
  s1 = 80
  s2 = 76
  s3 = 91
  s4 = 80
  s5 = 89
  avg = (s1+s2+s3+s4+s5)/5
  print("Average marks: ", avg)
