#! python3
#BZOJ Online PKer Version 2.0
#A Simple PKer of BZOJ
#Code is ugly because time is limited.
#Please run it under the environment Python 3
#Powered by Tony Zhao
#https://tonyzhao.xyz/bzoj-toolkits
import urllib.request, re, sys, platform

if (len(sys.argv) != 3 and len(sys.argv) != 4) or sys.argv[1] == '--help' or sys.argv[1] == '-h' :
	print("Project Comparison by Tony Zhao")
	print("A Simple PKer of BZOJ.")
	print("Version 2.0")
	if platform.system() == "Windows":
		print("Usage: py %s <First Person> <Second Person> (<Output file>)" % sys.argv[0])
	else:
		print("Usage: python3 %s <First Person> <Second Person> (<Output file>)" % sys.argv[0])
	exit()

URL = "http://www.lydsy.com/JudgeOnline/userinfo.php?user="
PersonA = sys.argv[1]
PersonB = sys.argv[2]
File = 'THISISNOTAFILE'

if len(sys.argv) == 4:
	File = sys.argv[3]

ProblemsA = urllib.request.urlopen(URL + PersonA).read().decode('utf-8')
ProblemsB = urllib.request.urlopen(URL + PersonB).read().decode('utf-8')

ProblemPattern = re.compile(r'function p\(id\){document\.write\("<a href=problem\.php\?id="\+id\+">"\+id\+" </a>"\);}\n(.+?)</script>')
SplitPattern = re.compile(r'p\((.+?)\);')

ProblemsA = SplitPattern.findall(ProblemPattern.findall(ProblemsA)[0])
ProblemsB = SplitPattern.findall(ProblemPattern.findall(ProblemsB)[0])

OnlyA = list(set(ProblemsA).difference(set(ProblemsB)))
Both  = list(set(ProblemsA).intersection(set(ProblemsB)))
OnlyB = list(set(ProblemsB).difference(set(ProblemsA)))

if File != 'THISISNOTAFILE':
	FOutput = open(File,"w")
	cnt = 0
	FOutput.write("Problems only %s has accepted:\n" % PersonA)
	for i in OnlyA:
		cnt += 1
		FOutput.write("%s   " % i)
		if cnt % 10 == 0 :
			FOutput.write("\n")
	cnt = 0
	FOutput.write("\nProblems both have accepted:\n")
	for i in Both:
		cnt += 1
		FOutput.write("%s   " % i)
		if cnt % 10 == 0 :
			FOutput.write("\n")
	cnt = 0
	FOutput.write("\nProblems only %s has accepted:\n" % PersonB)
	for i in OnlyB:
		cnt += 1
		FOutput.write("%s   " % i)
		if cnt % 10 == 0 :
			FOutput.write("\n")
else:
	cnt = 0
	print("Problems only %s has accepted:\n" % PersonA, end = '')
	for i in OnlyA:
		cnt += 1
		print("%s   " % i, end = '')
		if cnt % 10 == 0 :
			print('')
	cnt = 0
	print("\nProblems both have accepted:\n")
	for i in Both:
		cnt += 1
		print("%s   " % i, end = '')
		if cnt % 10 == 0 :
			print('')
	cnt = 0
	print("\nProblems only %s has accepted:\n" % PersonB, end = '')
	for i in OnlyB:
		cnt += 1
		print("%s   " % i, end = '')
		if cnt % 10 == 0 :
			print('')
	print('')
