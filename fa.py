import sys
import urllib2
import time
def main():
  
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
#    name = 'World'
#  print 'Howdy', name
 # print u"\u9FC0 \u9FC1"
 # print '"

    url = 'https://cp.adelaide.edu.au/courses/details.asp?year=2016&course=104230+1+3620+1'
#  url2 = 'https://cp.adelaide.edu.au/courses/details.asp?year=2016&course=104254+1+3620+1'
 # im = urllib2.urlopen(url2)
# im2= im.read()
'''
  while 1:
    fa = urllib2.urlopen(url)
    fa2 =  fa.read()
    print  "checking FA empty tute availability ....... ",9-fa2.count('FULL', 0,len(fa2))," free spot at the moment"
    print  "----------------------------------------------------------------------"
    print " last checked:  ", time.asctime(time.localtime())
    print  "----------------------------------------------------------------------"
#  print  im2.count('FULL', 0,len(im2))  '''

while 1:
       fa = urllib2.urlopen('https://cp.adelaide.edu.au/courses/details.asp?year=2016&course=104230+1+3620+1')
       fa2 =  fa.read()
       if fa2.count('FULL', 0,len(fa2)) != 9 :
          print " free spot in FA now"
          print " last checked:  ", time.asctime(time.localtime())    
       else:
             time.sleep(30)
             print "still checking.....", fa2.count('FULL', 0,len(fa2))," last checked:  ",time.asctime(time.localtime())    
            

if __name__ == '__main__':
  main()
	
