#! python3
#Project Herodotus Version 0.9.5
#A simple submission history traker of BZOJ
#Code is ugly because time is limited.
#Please run it under the environment Python 3
#Powered by Tony Zhao
#https://tonyzhao.xyz/bzoj-toolkits

import urllib.request, re, sys, platform

Person = 'THISISNOTAPERSON'
Year = '10000000'
Month = '10000000'
Day = '10000000'
File = 'THISISNOTAFILE'
AnotherUser = 'THISISNOTAPERSON'

if len(sys.argv) == 1 or sys.argv[1] == '--help' or sys.argv[1] == '-h' :
	print("Project Herodotus by Tony Zhao")
	print("A simple submission history traker of BZOJ.")
	print("Beta Version v0.9.5")
	if platform.system() == "Windows":
		print("Usage: py %s [Options]" % sys.argv[0])
	else:
		print("Usage: python3 %s [Options]" % sys.argv[0])
	print("Options:")
	print("	--help,   -h                     Show this help information.")
	print("	--name,   -n               BZOJ ID of the person.(Necessery)")
	print("	--year,   -y              Year of the deadline.(Default INF)")
	print("	--month,  -m             Month of the deadline.(Default INF)")
	print("	--day,    -d               Day of the deadline.(Default INF)")
	print("	--output, -o          Specify the output file of the result.")
	print("	--compare,-c Compare the result with another user's Problem.")
	exit()

now = 1
while now < len(sys.argv):
	if sys.argv[now] == '--name' or sys.argv[now] == '-n' :
		if now + 1 >= len(sys.argv):
			exit()
		Person = sys.argv[now + 1]
		now += 1
	elif sys.argv[now] == '--year' or sys.argv[now] == '-y' :
		if now + 1 >= len(sys.argv):
			exit()
		Year = sys.argv[now + 1]
		now += 1
	elif sys.argv[now] == '--month' or sys.argv[now] == '-m' :
		if now + 1 >= len(sys.argv):
			exit()
		Month = sys.argv[now + 1]
		now += 1
	elif sys.argv[now] == '--day' or sys.argv[now] == '-d' :
		if now + 1 >= len(sys.argv):
			exit()
		Day = sys.argv[now + 1]
		now += 1
	elif sys.argv[now] == '--output' or sys.argv[now] == '-o' :
		if now + 1 >= len(sys.argv):
			exit()
		File = sys.argv[now + 1]
		now += 1
	elif sys.argv[now] == '--compare' or sys.argv[now] == '-c' :
		if now + 1 >= len(sys.argv):
			exit()
		AnotherUser = sys.argv[now + 1]
		now += 1
	else:
		print("'%s' is not a recognized Command." % sys.argv[now])
		exit()
	now += 1
if Person == 'THISISNOTAPERSON':
	print("No ID Specified.")
	exit()

URL = 'http://www.lydsy.com/JudgeOnline/status.php?problem_id=&user_id=' + Person + '&language=-1&jresult=4'
ProblemPattern = re.compile("<a href='problem\.php\?id=(.+?)'>")
YearPattern = re.compile(r"<td>(\d+?)-\d*-\d* \d*:\d*:\d*</tr>")
MonthPattern = re.compile(r"<td>\d*-(\d+?)-\d* \d*:\d*:\d*</tr>")
DayPattern = re.compile(r"<td>\d*-\d*-(\d+?) \d*:\d*:\d*</tr>")
URLPattern = re.compile(r"Previous Page</a>]&nbsp;&nbsp;\[<a href=(.+?)>Next Page</a>")
TopPattern = re.compile(r"&jresult=4&top=(.+?)&prevtop=\d*")
PrevtopPattern = re.compile(r"&jresult=4&top=\d*&prevtop=(.+)")

AllProblems = []
AllYears = []
AllMonths = []
AllDays = []

FinalProblems = []

while True:
	History = urllib.request.urlopen(URL).read().decode('utf-8')
	Problems = ProblemPattern.findall(History)
	Years = YearPattern.findall(History)
	Months = MonthPattern.findall(History)
	Days = DayPattern.findall(History)
	URL ="http://www.lydsy.com/JudgeOnline/" + URLPattern.findall(History)[0]
	Top = TopPattern.findall(URL)[0]
	Prevtop= PrevtopPattern.findall(URL)[0]
	if Top == Prevtop:
		break
	if len(AllProblems) != 0:
		Problems = Problems[1:]
		Years = Years[1:]
		Months = Months[1:]
		Days = Days[1:]
	AllProblems.extend(Problems)
	AllYears.extend(Years)
	AllMonths.extend(Months)
	AllDays.extend(Days)

for i in range(len(AllProblems)):
	if int(Year) < int(AllYears[i]): continue
	if int(Year) == int(AllYears[i]) and int(Month) < int(AllMonths[i]): continue
	if int(Year) == int(AllYears[i]) and int(Month) == int(AllMonths[i]) and int(Day) < int(AllDays[i]): continue
	FinalProblems.append(AllProblems[i])

FinalProblems = list(set(FinalProblems))

if AnotherUser != 'THISISNOTAPERSON':
	URL = "http://www.lydsy.com/JudgeOnline/userinfo.php?user=" + AnotherUser
	Problems = urllib.request.urlopen(URL).read().decode('utf-8')
	ProblemPattern = re.compile(r'function p\(id\){document\.write\("<a href=problem\.php\?id="\+id\+">"\+id\+" </a>"\);}\n(.+?)</script>')
	SplitPattern = re.compile(r'p\((.+?)\);')
	Problems = SplitPattern.findall(ProblemPattern.findall(Problems)[0])
	FinalProblems = list(set(FinalProblems).difference(set(Problems)))


if File != 'THISISNOTAFILE':
	FOutput = open(File,"w")
	cnt = 0
	for i in FinalProblems:
		cnt += 1
		FOutput.write("%s   " % i)
		if cnt % 5 == 0 :
			FOutput.write("\n")
else:
	cnt = 0
	for i in FinalProblems:
		cnt += 1
		print("%s   " % i, end = '')
		if cnt % 10 == 0 :
			print('')
	print('')
