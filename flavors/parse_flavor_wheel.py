import os 
import json
import sys
import getopt
import fuzzywuzzy.process as pro


def traverse(data, p="None"):
	# identify flavor categories by traversing dictionry 
	# structured imported from Json file
	flavors = [(str(data['flavor']), str(p))]
	if 'children' in data:
		for child in data['children']:
			flavors.extend(traverse(child, data['flavor']))
	fl = []
	for f in flavors:
		fl.append((f[0], f[1]) if f[0]!=f[1] else (f[0], "None"))
	
	return fl


def score(txt, d):
	# Search flavors categories from a given Json file.
	parse = set(pro.extract(txt, set(d.values()+d.keys())))
	if not parse:
		return 

	parse = [s for s in parse if s[1]>10.]
	average = sum([s[1] for s in parse ])/len(parse) if len(parse)>0 else 0
	parse = [s for s in parse if s[1]>average]
	categories = []
	for i in parse:
		node = i[0]
		t = []
		while node != "None":
			t.append(node)
			node = d[node]
		categories.append(t[::-1])
	return categories


def Main(argv):
	wheel_file = ''
	input_file = ''
	
	try:
	  	opts, args = getopt.getopt(sys.argv[1:],"i:f:")
	
	except getopt.GetoptError as e:
		print (str(e))	
		print("Usage: %s -i wheel -f file" % sys.argv[0])
	  	sys.exit(2)

	if not len(opts):
		print("Usage: %s -i wheel -f file" % sys.argv[0])
		sys.exit(2)
	for o, a in opts:
		if o == '-i':
		    wheel_file = a
		elif o == '-f':
		    input_file = a

	print ("use Wheel file : %s and tasting file: %s" %  (wheel_file, input_file) )
	return (wheel_file, input_file)


def run(wheel_file, input_file):
	'''using the files names from user parameters to
	run the traverse and the score fuctions.
	the output file is /tmp/categies.html '''

	#wheel_file = os.path.join( os.path.realpath(os.getcwd()), 'scaa_flavor_wheel.json')
	with open(wheel_file) as json_data:
	    data = json.load(json_data)

	data_tree = dict(traverse(data))

	#input_file = os.path.join( os.path.realpath(os.getcwd()), 'tasting_notes_tt.json')''
	f = open('/tmp/categories.html','w')	
	output = "<html>"
	with open(input_file) as json_data:
	    data = json.load(json_data)
	    for txt in data:
	    	output = output + "<p>%s</p><br\><pre>%s</pre><br\>" %(txt, score(txt, data_tree ) )

	output = output+"</html>"
	try:
		f.write(output.encode('utf-8'))
		print "Please check the output /tmp/categories.html"
	except exception as e:
		print str(e)
	finally:
		f.close()


if __name__ == '__main__':
	wheel_file, input_file = Main(sys.argv[1:])
	
	try:
		run(wheel_file, input_file)
	except:
		print "run methods required two inputs files : the Wheel file and the Tasting file, and both in Json format"


	